import json

import jwt
from flask import Blueprint, current_app, request,jsonify
from util.jwt import get_millisecond

auth = Blueprint("auth", __name__)


@auth.route("/auth", methods=["POST"])
def index():
    try:
        weekly_key = json.loads(request.data.decode("UTF-8"))["key"]
        if weekly_key == current_app.config["ADMIN_KEY"]:
            return jsonify({"access": "true"})

        decoded = jwt.decode(request.headers["Authorization"], current_app.config["JWT_SECRET"], algorithms="HS256")
        millisecond = get_millisecond(0)

        if int(decoded["exp"]) > millisecond and weekly_key == current_app.config["WEEKLY_KEY"]:
            return jsonify({"access": "true"})
        else:
            return jsonify({"access": "false"})
    except Exception:
        return jsonify({"access": "false"})
