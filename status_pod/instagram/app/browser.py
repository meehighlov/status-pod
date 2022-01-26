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

    chrome = webdriver.Remote(
        command_executor=config.SELENOID_URL,
        desired_capabilities=capabilities
    )

    # chrome = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)

    return chrome
