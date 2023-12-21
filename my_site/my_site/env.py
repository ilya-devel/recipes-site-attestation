import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# if os.path.exists(dotenv_path):
#     load_dotenv(dotenv_path)


load_dotenv()


class Settings(BaseSettings):
    SECRET_KEY: str
    DB_ENGINE: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str

    class Config:
        env_file = dotenv_path


settings = Settings()
