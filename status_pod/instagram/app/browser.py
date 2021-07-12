from selenium import webdriver
from status_pod.app.config import config


chrome = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)


def create_browser_instance(*args, **kwargs):
    pass
