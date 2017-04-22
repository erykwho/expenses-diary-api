from flask import Flask
from project.expense import expense
from project.category import category
from project.payment_origin import payment_origin

app = Flask(__name__)

app.register_blueprint(expense)
app.register_blueprint(category)
app.register_blueprint(payment_origin)
