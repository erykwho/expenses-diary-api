import os
import traceback
from datetime import datetime

from config.config import Config


def new(owner):
    log_path = Config().LOG_PATH
    return Logger(owner, log_path)


class Logger(object):
    def __init__(self, owner, log_path):
        self.owner = owner
        self.__log_path = log_path

    def write_file(self, category, message):

        try:
            m = "{}||{}||{}||{}".format(datetime.now(), category, self.owner, message)
            with open(self.__log_path, "a") as log_file:
                print(m)
                log_file.write("{}{}".format(m, os.linesep))
        except Exception as e:
            print(str(e))
            print(traceback.format_exc())

    def info(self, message):
        self.write_file("Info", message)

    def error(self, message):
        self.write_file("Error", message)
