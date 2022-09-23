from config import flask_config
from flask import Flask
from flask_cors import CORS
import os 

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

def register_router(flask_app: Flask):
    # router들을 등록 해주는 곳
    from router.twitter_router.twitter import twitter
    from router.auth_router.auth import auth
    
    flask_app.register_blueprint(twitter)
    flask_app.register_blueprint(auth)

    # flask app의 request/response들과 매번 함께 실행 할 함수 정의
    @flask_app.before_request
    def before_my_request():
        print("before my request")

    @flask_app.after_request
    def after_my_request(res):
        print("after my request", res.status_code)
        return res


def create_app():
    # 앱 설정
    app = Flask(__name__)

    CORS(app)

    app.config.from_object((get_flask_env()))
    register_router(app)
    return app


def get_flask_env():
    # 환경변수에 따라 config나누기
    if flask_config.Config.ENV == "prod":
        print("product")
        return "config.flask_config.prodConfig"
    elif flask_config.Config.ENV == "dev":
        print("developer")
        return "config.flask_config.devConfig"
