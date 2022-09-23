import os

from dotenv import load_dotenv

load_dotenv(verbose=True)


class Config(object):
    ENV = os.getenv("ENV")
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("JWT_SECRET")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET = os.getenv("JWT_SECRET")
    OAUTH2_CLIENT_ID = os.getenv("OAUTH2_CLIENT_ID")
    OAUTH2_CLIENT_SECRET = os.getenv("OAUTH2_CLIENT_SECRET")

    API_BASE_URL = os.getenv("API_BASE_URL")
    AUTHORIZATION_BASE_URL = API_BASE_URL + "/oauth2/authorize"
    TOKEN_URL = API_BASE_URL + "/oauth2/token"

    JWT_SECRET = os.getenv("JWT_SECRET")
    WEEKLY_KEY = os.getenv("WEEKLY_KEY")
    ADMIN_KEY = os.getenv("ADMIN_KEY")


class devConfig(Config):
    # DEBUG = True
    BASE_URL = "http://localhost:5002"
    OAUTH2_REDIRECT_URI = BASE_URL + "/twitter/callback"


class prodConfig(Config):
    # DEBUG = False
    BASE_URL = os.environ["BASE_URL"]
    OAUTH2_REDIRECT_URI = BASE_URL + "/twitter/callback"
