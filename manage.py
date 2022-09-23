import os

from app.init import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True,ssl_context=('./server.crt', './server.key'))

# https://www.woolog.dev/backend/flask/using-flask-with-smart-structure/#appinitpy
