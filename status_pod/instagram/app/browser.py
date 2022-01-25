from selenium import webdriver
from status_pod.app.config import config


def create_browser_instance(*args, **kwargs):
    browser_name = kwargs.get('browser', 'chrome')

    chrome = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)

    return chrome
