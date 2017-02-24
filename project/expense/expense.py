import flask_restful as restful
from logger.logger import new

logger = new("Expense")


class Expense(restful.Resource):
    def __init__(self):
        pass

    @staticmethod
    def get():
        logger.info("GET - Expense")
        return "All Expenses", 200
