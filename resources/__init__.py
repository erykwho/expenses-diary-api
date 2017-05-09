import flask_login
from flask import Flask

from resources.authentication import authentication
from resources.category import category
from resources.expense import expense
from resources.payment_origin import payment_origin
from resources.user import user

app = Flask(__name__)

app.register_blueprint(expense)
app.register_blueprint(category)
app.register_blueprint(payment_origin)
app.register_blueprint(user)
app.register_blueprint(authentication)

# Setup of login session manager
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
