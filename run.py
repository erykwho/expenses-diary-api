from project import app
from config.config import Config
from logger.logger import new

logger = new("Run")

if __name__ == '__main__':
    app.config.from_object(Config())
    host = '0.0.0.0'
    port = app.config.get("PORT")
    logger.info("Iniciando aplicacao no host {} e porta {}".format(host, port))
    app.run(
        host=host,
        port=port
    )
