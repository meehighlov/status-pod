from datetime import datetime, timedelta

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from status_pod.instagram.profile.common.login import login, close_popups_after_login


COMMENT_CLASS = 'QzzMF.Igw0E.IwRSH.eGOV_.vwCYk'


def get_posts_for_current_context(context):
    return context.find_elements(By.TAG_NAME, value='article')


def get_post_date(post) -> datetime:
    elem_with_dt = post.find_element(By.CLASS_NAME, value='_1o9PC.Nzb55')
    dt: str = elem_with_dt.get_attribute('datetime')
    return datetime.strptime(dt, '%Y-%m-%dT%H:%S:%f.000Z')  # TODO set format as variable


def open_feed(browser):
    login(browser)
    close_popups_after_login(browser)


def get_post_owner_name(post):
    return post.find_element(By.CLASS_NAME, value='sqdOP.yWX7d._8A5w5.ZIAjV').text


def get_first_comment_as_element(post):
    return post.find_element(By.CLASS_NAME, value=COMMENT_CLASS)


def has_post_comments(post):
    try:
        post.find_element(By.CLASS_NAME, value=COMMENT_CLASS)
    except NoSuchElementException:
        return False
    return True


def get_comment_owner_name(comment) -> str:
    return comment.find_element(By.CLASS_NAME, value='FPmhX.notranslate.MBL3Z').text


def get_comment_content(post) -> str:
    comment = get_first_comment_as_element(post)
    button_more_class = 'sXUSN'

    # ищем по finds так как кнопки "еще" может не быть, если коммент короткий
    button_more = comment.find_elements(By.CLASS_NAME, value=button_more_class)
    if button_more:
        # разворачиваем коммент
        button_more[0].click()

    content = comment.find_element(By.CLASS_NAME, value='_8Pl3R').text

    return content


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
    pass


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

    stories_and_posts_pipeline = get_main_layout(browser)

    while post_date < edge_date:
        posts = get_posts_for_current_context(stories_and_posts_pipeline)
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

        scroll_down_feed(browser)


def analyze_posts(browser):
    with browser:
        analyze_posts_(browser=browser)
