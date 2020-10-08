import os
import dotenv


dotenv.load_dotenv()


class Config:
    USER_NAME = os.getenv('USER_NAME')
    TOKEN = os.getenv('TOKEN')
    MY_CHAT_ID = os.getenv('MY_CHAT_ID')
    DB_NAME = os.getenv('DB_NAME')


config = Config()
