from flask import Flask
from route.ServerRoute import serverRoute
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.register_blueprint(serverRoute)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8011)