from flask import make_response, jsonify


class AuthenticationFailed(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.message = "Authentication Failed."
        self.status_code = 400

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.message

    @property
    def http_response(self):
        return make_response(jsonify(message=self.message), self.status_code)
