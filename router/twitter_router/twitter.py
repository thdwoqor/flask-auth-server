from flask import (
    Blueprint,
    current_app,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from requests_oauthlib import OAuth2Session
from util.jwt import create_jwt

twitter = Blueprint("twitter", __name__, url_prefix="/twitter", template_folder="../../templates")


def token_updater(token):
    session["oauth2_token"] = token


def make_session(token=None, state=None, scope=None):
    return OAuth2Session(
        client_id=current_app.config["OAUTH2_CLIENT_ID"],
        token=token,
        state=state,
        scope=scope,
        redirect_uri=current_app.config["OAUTH2_REDIRECT_URI"],
        auto_refresh_kwargs={
            "client_id": current_app.config["OAUTH2_CLIENT_ID"],
            "client_secret": current_app.config["OAUTH2_CLIENT_SECRET"],
        },
        auto_refresh_url=current_app.config["TOKEN_URL"],
        token_updater=token_updater,
    )


@twitter.route("/", methods=["GET"])
def index():
    scope = request.args.get("scope", "identify guilds guilds.members.read")
    discord = make_session(scope=scope.split(" "))
    authorization_url, state = discord.authorization_url(current_app.config["AUTHORIZATION_BASE_URL"])
    session["oauth2_state"] = state
    return redirect(authorization_url)


@twitter.route("/callback", methods=["GET"])
def callback():
    if request.values.get("error"):
        return request.values["error"]

    discord = make_session(state=session.get("oauth2_state"))
    token = discord.fetch_token(current_app.config["TOKEN_URL"], client_secret=current_app.config["OAUTH2_CLIENT_SECRET"], authorization_response=request.url)
    session["oauth2_token"] = token
    return redirect(url_for(".result"))


@twitter.route("/result", methods=["GET"])
def result():
    discord = make_session(token=session["oauth2_token"])

    user = discord.get(current_app.config["API_BASE_URL"] + "/users/@me").json()
    guilds = discord.get(current_app.config["API_BASE_URL"] + "/users/@me/guilds").json()

    id = f"{user['username']}#{user['discriminator']}"

    for data in guilds:
        if data["id"] == "146930111478890496":
            return render_template("success.html", jwt=create_jwt(id), id=id)

    return render_template("fail.html")
