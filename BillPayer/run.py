from settings import ConfigEnvironment
from billpayer import create_app


app = create_app("default")

if __name__ == "__main__":
    ce = ConfigEnvironment("./.env")
    ce.load_environment()

    app.run(host="0.0.0.0")

