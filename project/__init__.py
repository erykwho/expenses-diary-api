from flask import Flask
from project.expense import expense

app = Flask(__name__)

app.register_blueprint(expense)
