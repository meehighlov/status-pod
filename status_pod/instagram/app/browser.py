from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from status_pod.app.config import config


# opt = Options()
# if config.HEADLESS_MODE:
#     opt.add_argument("--headless")

chrome = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)


def create_browser_instance(*args, **kwargs):
    pass
