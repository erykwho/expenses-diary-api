from flask import Flask
from flask_cors import CORS
from resources.expense import expense
from resources.category import category
from resources.payment_origin import payment_origin
from resources.user import user

app = Flask(__name__)

app.register_blueprint(expense)
app.register_blueprint(category)
app.register_blueprint(payment_origin)
app.register_blueprint(user)

CORS(app)