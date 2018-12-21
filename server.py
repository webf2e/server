from flask import Flask
from route.ServerRoute import serverRoute

app = Flask(__name__)

app.register_blueprint(serverRoute)


if __name__ == '__main__':
    app.run()
