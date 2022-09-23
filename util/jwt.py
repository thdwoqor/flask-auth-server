import os
from datetime import datetime, timedelta

import jwt


def get_millisecond(seconds):
    epoch = datetime.utcfromtimestamp(0)
    millisecond = int((datetime.utcnow() + timedelta(seconds=seconds) - epoch).total_seconds() * 1000.0)
    return millisecond


def create_jwt(id):
    millisecond = get_millisecond(60 * 60 * 24 * 7)
    payload = {"id": id, "exp": millisecond}
    return jwt.encode(payload, os.environ["JWT_SECRET"], algorithm="HS256")
