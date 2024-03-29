import os

from dotenv import load_dotenv


load_dotenv()


cast_to = lambda type_: lambda *args, value: type_(value)


# TODO use pydantic
class Config:
    MAX_WAIT_ELEMENT_APPEARANCE_SEC = cast_to(int)
    CHROME_DRIVER_PATH = cast_to(str)
    REPORT_PATH = cast_to(str)
    HEADLESS_MODE = cast_to(bool)

    INSTAGRAM_LOGIN = cast_to(str) # noqa
    INSTAGRAM_PASSWORD = cast_to(str)  # noqa
    INSTAGRAM_URL = cast_to(str)  # noqa
    TIMEOUT_FOR_INSTA_TASK_EXECUTION_SEC = cast_to(int) # noqa
    WAIT_FOR_INSTA_STALE_ELEMENT_SEC = cast_to(int)
    MAX_INSTA_POSTS_AMOUNT_FOR_ANALYSYS = cast_to(int)

    USER_NAME = cast_to(str)
    TOKEN = cast_to(str)
    MY_CHAT_ID = cast_to(str)
    DB_NAME = cast_to(str)

    def __init__(self, **kwargs):
        for var, raw_value in kwargs.items():
            if hasattr(self, var):
                value = getattr(self, var)(value=raw_value)
                setattr(self, var, value)


config = Config(**os.environ)
