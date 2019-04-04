from flask import Flask
from route.ServerRoute import serverRoute
from route.GitRoute import gitRoute
from route.FirewallRoute import firewallRoute
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.register_blueprint(serverRoute)
app.register_blueprint(gitRoute)
app.register_blueprint(firewallRoute)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8011)