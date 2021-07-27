import time
from datetime import datetime, timedelta
from functools import wraps

from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException
)
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from status_pod.app.config import config
from status_pod.instagram.profile.common.login import login, close_popups_after_login


COMMENT_CLASS = 'QzzMF.Igw0E.IwRSH.eGOV_.vwCYk'


def suppress_interaction_exceptions(return_this_on_suppress):
    def suppress_interaction_exceptions_wrapper(f):
        @wraps(f)
        def suppressor(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except (NoSuchElementException,
                    StaleElementReferenceException,
                    ElementClickInterceptedException):
                return return_this_on_suppress
        return suppressor
    return suppress_interaction_exceptions_wrapper


def wait(context, element):
    wait = WebDriverWait(context, timeout=config.MAX_WAIT_ELEMENT_APPEARANCE_SEC)
    wait.until(lambda p: p.find_element(By.TAG_NAME, value=element))


def get_posts_for_current_context(context):
    return context.find_elements(By.TAG_NAME, value='article')


@suppress_interaction_exceptions(return_this_on_suppress=datetime.utcnow() + timedelta(days=1))
def get_post_date(post) -> datetime:
    elem_with_dt = post.find_element(By.CLASS_NAME, value='_1o9PC.Nzb55')
    dt: str = elem_with_dt.get_attribute('datetime')
    return datetime.strptime(dt, '%Y-%m-%dT%H:%S:%f.000Z')  # TODO set format as variable


def open_feed(browser):
    login(browser)
    close_popups_after_login(browser)


@suppress_interaction_exceptions(return_this_on_suppress='post_owner')  # TODO make random default name
def get_post_owner_name(post):
    return post.find_element(By.CLASS_NAME, value='sqdOP.yWX7d._8A5w5.ZIAjV').text


def get_first_comment_as_element(post):
    return post.find_element(By.CLASS_NAME, value=COMMENT_CLASS)


@suppress_interaction_exceptions(return_this_on_suppress=False)
def has_post_comments(post):
    try:
        post.find_element(By.CLASS_NAME, value=COMMENT_CLASS)
    except NoSuchElementException:
        return False
    return True


@suppress_interaction_exceptions(return_this_on_suppress='comment_owner')
def get_comment_owner_name(comment) -> str:
    return comment.find_element(By.CLASS_NAME, value='FPmhX.notranslate.MBL3Z').text


def try_get_text_of_stale_element(
        parent,
        by,
        value,
        tries=3,
        timeout=config.WAIT_FOR_INSTA_STALE_ELEMENT_SEC,
        default_text=''
):
    for _ in range(tries):
        try:
            return parent.find_element(by=by, value=value).text
        except StaleElementReferenceException as e:
            time.sleep(timeout)
    return default_text


@suppress_interaction_exceptions(return_this_on_suppress='')
def get_comment_content(post) -> str:
    comment = get_first_comment_as_element(post)
    button_more_class = 'sXUSN'

    # ищем по finds так как кнопки "еще" может не быть, если коммент короткий
    button_more = comment.find_elements(By.CLASS_NAME, value=button_more_class)
    if button_more:
        # разворачиваем коммент
        try:
            button_more[0].click()
        except ElementClickInterceptedException as e:
            # TODO logging
            return ''

    content = try_get_text_of_stale_element(comment, By.CLASS_NAME, '_8Pl3R')

    return content


@suppress_interaction_exceptions(return_this_on_suppress=False)
def is_first_comment_written_by_post_owner(post):
    comment_e = get_first_comment_as_element(post)
    co = get_comment_owner_name(comment_e)
    po = get_post_owner_name(post)
    return co == po


def has_comment_triggers(comment: str):
    return True


def notify():
    pass


def scroll_down_feed(browser):
    ActionChains(browser).send_keys(Keys.PAGE_DOWN).perform()


def create_post_hash(post):
    post_owner = get_post_owner_name(post)
    post_date = get_post_date(post)

    return hash(post_owner + str(post_date))


def get_main_layout(browser) -> WebElement:
    return browser.find_element(
        By.XPATH,
        value='/html/body/div[1]/div/div/section/main/section/div/div[2]'
    )


def analyze_posts_(browser):
    open_feed(browser)

    post_date = datetime.utcnow()  # temporary
    edge_date = post_date + timedelta(days=1)  # temporary
    viewed_posts = set()

    posts_amount_to_check = config.MAX_INSTA_POSTS_AMOUNT_FOR_ANALYSYS
    while len(viewed_posts) < posts_amount_to_check:
        posts = get_posts_for_current_context(browser)
        for post in posts:

            post_hash = create_post_hash(post)
            if post_hash in viewed_posts:
                continue

            viewed_posts.add(post_hash)

            if not has_post_comments(post):
                continue

            if not is_first_comment_written_by_post_owner(post):
                continue

            comment = get_comment_content(post)

            if has_comment_triggers(comment):
                notify()

            post_date = get_post_date(post)

            print('already viewed:', len(viewed_posts))

        scroll_down_feed(browser)


def analyze_posts(browser):
    with browser:
        analyze_posts_(browser=browser)
