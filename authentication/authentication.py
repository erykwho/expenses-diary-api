from functools import wraps

from flask import request, abort

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        user_id = request.headers.get('User-Id')
        if user_id:
            return f(*args, **kwargs)
        else:
            return abort(401)

    return wrap
