from selenium import webdriver
from status_pod.app.config import config


def create_browser_instance(*args, **kwargs):
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "96.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    # chrome = webdriver.Remote(
    #     command_executor=config.SELENOID_URL,
    #     desired_capabilities=capabilities
    # )

    GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
    CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.binary_location = GOOGLE_CHROME_PATH

    # chrome = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)
    chrome = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

    return chrome
