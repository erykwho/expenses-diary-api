import flask_restful as restful
# from project import app


class Expense(restful.Resource):
    def __init__(self):
        pass

    @staticmethod
    def get():
        return "All Expenses", 200
