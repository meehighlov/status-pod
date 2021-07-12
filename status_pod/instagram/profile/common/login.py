from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from status_pod.app.config import config


def login(browser):
    browser.get(config.INSTAGRAM_URL)

    wait = WebDriverWait(browser, timeout=config.MAX_WAIT_ELEMENT_APPEARANCE_SEC)

    wait.until(lambda p: p.find_element(By.TAG_NAME, value='input'))

    username = browser.find_element(By.NAME, value='username')
    password = browser.find_element(By.NAME, value='password')

    username.send_keys(config.INSTAGRAM_LOGIN)
    password.send_keys(config.INSTAGRAM_PASSWORD)

    submit_button = browser.find_element(By.CLASS_NAME, value='Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB')
    submit_button.click()


def close_popups_after_login(browser):
    wait = WebDriverWait(browser, timeout=config.MAX_WAIT_ELEMENT_APPEARANCE_SEC)

    wait.until(lambda p: p.find_element(By.CLASS_NAME, value='cmbtv'))

    not_now_button = browser.find_element(By.CLASS_NAME, value='sqdOP.yWX7d.y3zKF')
    not_now_button.click()

    wait.until(lambda p: p.find_element(By.CLASS_NAME, value='mt3GC'))

    disable_notifications_button = browser.find_element(By.CLASS_NAME, value='aOOlW.HoLwm')
    disable_notifications_button.click()
