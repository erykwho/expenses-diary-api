from flask_login import UserMixin

from resources import login_manager


class User(UserMixin):

    def __init__(self, id):
        self.id = id


@login_manager.user_loader
def load_user(id):
    user = User(id)
    return user


@login_manager.request_loader
def request_loader(id):
    user = User(id)
    return user
