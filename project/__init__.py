from flask import Flask
from project.expense import expense
from project.category import category

app = Flask(__name__)

app.register_blueprint(expense)
app.register_blueprint(category)
