from datetime import datetime, timedelta

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from status_pod.instagram.profile.common import login, close_popups_after_login



def get_posts_for_current_context(browser):
    post_classes = {
        'single': '_8Rm4L.bLWKA M9sTE.L_LMM SgTZ1.ePUX4',
        'carousel': '_8Rm4L.bLWKA M9sTE.L_LMM.SgTZ1.Tgarh.ePUX4'
    }

    return [
        *browser.find_elements(By.CLASS_NAME, value=post_classes['single']),
        *browser.find_elements(By.CLASS_NAME, value=post_classes['carousel'])
    ]


def get_post_date(post):
    return ''


def open_feed(browser):
    login(browser)
    close_popups_after_login(browser)


def get_post_owner_name(post):
    return ''


def first_comment_is_written_by_post_owner(post):
    return True


def get_first_comment(post):
    return ''


def has_comment_triggers(comment: str):
    return True


def notify():
    pass


def scroll_down_feed():
    pass


def create_post_hash(post):
    post_owner = get_post_owner_name(post)
    post_date = get_post_date(post)

    return hash(post_owner + post_date)


def analyze_posts(browser):
    open_feed(browser)

    post_date = datetime.utcnow()  # temporary
    edge_date = post_date + timedelta(days=1)  # temporary
    viewed_posts = set()

    while post_date < edge_date:
        posts = get_posts_for_current_context(browser)
        for post in posts:

            post_hash = create_post_hash(post)
            if post_hash in viewed_posts:
                continue

            viewed_posts.add(post_hash)

            if not first_comment_is_written_by_post_owner(post):
                continue

            comment = get_first_comment(post)

            if has_comment_triggers(comment):
                notify()

            post_date = get_post_date(post)

        scroll_down_feed(browser)
