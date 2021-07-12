from typing import Set

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from status_pod.app.config import config
from status_pod.instagram.app.meta import SubscriptionInfo


def open_profile(browser):
    wait = WebDriverWait(browser, timeout=config.MAX_WAIT_ELEMENT_APPEARANCE_SEC)
    wait.until(lambda p: p.find_element(By.CLASS_NAME, value='gmFkV'))
    profile_icon_as_button = browser.find_element(By.CLASS_NAME, value='gmFkV')
    profile_icon_as_button.click()


def get_users_amount(link_text: str):
    """
        текущий формат текста ссылки: 'n подписчиков'
    """

    return int(link_text.split()[0].rstrip())


def fetch_nicknames_from_list(browser, users_amount, window_with_list) -> Set[str]:
    print('users need to fetch:', users_amount)

    wait = WebDriverWait(browser, timeout=config.MAX_WAIT_ELEMENT_APPEARANCE_SEC)
    wait.until(lambda p: p.find_element(By.TAG_NAME, value='li'))

    users_meta = []
    while len(users_meta) < users_amount:
        action = ActionChains(browser)
        action.send_keys([Keys.TAB] * 2).perform()

        wait.until(lambda p: p.find_element(By.TAG_NAME, value='li'))
        users_meta = window_with_list.find_elements(By.TAG_NAME, value='li')

        print('found:', len(users_meta), 'done:', f'{round((len(users_meta) / users_amount) * 100, 1)}%')

    user_nicknames = window_with_list.find_elements(By.CLASS_NAME, value='FPmhX.notranslate._0imsa')
    return set(elem.text for elem in user_nicknames)


def get_users_info(browser, who: str):
    user_list_types = {
        'follows_me': 'followers',  # TODO switch locale - now it depends on locale
        'i_am_follow': 'following'  # TODO switch locale - now it depends on locale
    }
    wait = WebDriverWait(browser, timeout=config.MAX_WAIT_ELEMENT_APPEARANCE_SEC)
    wait.until(lambda p: p.find_element(By.CLASS_NAME, value='zwlfE'))
    profile_main_buttons = browser.find_element(By.CLASS_NAME, value='zwlfE')

    users_number_as_button = profile_main_buttons.find_element(
        By.PARTIAL_LINK_TEXT,
        value=user_list_types[who]
    )

    users_amount = get_users_amount(users_number_as_button.text)
    users_number_as_button.click()

    wait.until(lambda p: p.find_element(By.CLASS_NAME, value='isgrP'))

    users_list_window = browser.find_element(By.CLASS_NAME, value='isgrP')

    nicknames = fetch_nicknames_from_list(
        browser,
        users_amount,
        users_list_window
    )

    return SubscriptionInfo(
        users_amount=users_amount,
        nicknames=nicknames
    )


def close_window_with_users_list(browser):
    close_button = browser.find_element(By.CLASS_NAME, value='wpO6b')
    ActionChains(browser).click(close_button).perform()
