from project import app
from config.config import Config

if __name__ == '__main__':
    app.config.from_object(Config())
    app.run(
        host='0.0.0.0',
        port=app.config.get("PORT")
    )
