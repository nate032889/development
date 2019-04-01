from flask import Flask
from billpayer.config import config


def create_app(config_class):
    app = Flask(__name__)
    obj = config[config_class]
    app.config.from_object(obj)

    from billpayer.auth.views import auth
    from billpayer.main.views import main
    app.register_blueprint(auth)
    app.register_blueprint(main)

    return app
