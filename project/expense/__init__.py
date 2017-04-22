import flask_restful as restful
from flask import Blueprint # pragma: no cover

from project.expense.expense import Expenses, Expense


expense = Blueprint(
    'expense', __name__,
)


api = restful.Api()
api.init_app(expense)

api.add_resource(Expenses, '/v1/expenses')
api.add_resource(Expense, '/v1/expenses/<int:id>')

