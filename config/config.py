import inspect
import os
import sys

from config.singleton import Singleton


class BaseConfig(object):
    # DEBUG Config
    DEBUG = False

    # API Config
    TOKEN = os.environ["EXD_TOKEN"]

    # DB Config
    POSTGRESQL_HOST = os.environ['EXD_POSTGRESQL_HOST']
    POSTGRESQL_USER = os.environ['EXD_POSTGRESQL_USER']
    POSTGRESQL_PASS = os.environ['EXD_POSTGRESQL_PASS']
    POSTGRESQL_PORT = os.environ['EXD_POSTGRESQL_PORT']
    POSTGRESQL_DB = os.environ['EXD_POSTGRESQL_DB']

    # Http Config
    PORT = int(os.environ.get('EXD_PORT', 5000))

    # Log Config
    LOG_PATH = os.environ["EXD_LOG_PATH"]


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


class Config(object):
    __metaclass__ = Singleton

    def __init__(self):

        this_module = sys.modules[__name__]
        env = os.environ.get('APP_SETTINGS', 'DevelopmentConfig')
        self.config = getattr(this_module, env)

        attributes = inspect.getmembers(
            self.config, lambda a: not (inspect.isroutine(a)))
        for attr in attributes:
            if not (attr[0].startswith('__') or attr[0].startswith('_')):
                setattr(self, attr[0], attr[1])
