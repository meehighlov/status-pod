import os
import dotenv


dotenv.load_dotenv()


class Config:
    USER_NAME = os.getenv('USER_NAME')


config = Config()
