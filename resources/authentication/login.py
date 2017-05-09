import flask_restful as restful

from logger.logger import new

logger = new("Authentication")


class Login(restful.Resource):
    def __init__(self):
        pass

    @staticmethod
    def post():
        return {
            "message": "Logado.. ou não?"
        }, 420


class Logout(restful.Resource):
    def __init__(self):
        pass

    @staticmethod
    def post():
        return {
            "message": "Deslogado.. ou não?"
        }, 420