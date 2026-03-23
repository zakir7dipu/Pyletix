import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    APP_NAME = os.getenv("APP_NAME", "Zak Flet")
    APP_ENV = os.getenv("APP_ENV", "production")
    APP_DEBUG = os.getenv("APP_DEBUG", "false").lower() == "true"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # DB
    DB_CONNECTION = os.getenv("DB_CONNECTION", "sqlite")
    DB_DATABASE = os.path.join(BASE_DIR, os.getenv("DB_DATABASE", "storage/database.sqlite"))

    # Security
    APP_KEY = os.getenv("APP_KEY", "")

    # Mail
    MAIL_DRIVER = os.getenv("MAIL_DRIVER", "smtp")
    MAIL_HOST = os.getenv("MAIL_HOST", "localhost")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_ENCRYPTION = os.getenv("MAIL_ENCRYPTION")
    MAIL_FROM_ADDRESS = os.getenv("MAIL_FROM_ADDRESS")
    MAIL_FROM_NAME = os.getenv("MAIL_FROM_NAME", APP_NAME)
    
    @staticmethod
    def get(key, default=None):
        return os.getenv(key, default)

config = Config()
