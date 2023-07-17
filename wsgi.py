from src import create_app
from src.config.settings import CONFIG

app = create_app(**CONFIG)


if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True,
            port=CONFIG["PORT"],
            debug=CONFIG["DEBUG"])
