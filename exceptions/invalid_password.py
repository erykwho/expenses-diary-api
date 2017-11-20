from flask import make_response, jsonify


class InvalidPassword(Exception):
    """ Error when password is incorrect.

    Attributes:
        message (str): Error message

    Properties:
        http_response (JSON Serializable): Flask JSON response for this error
    """

    def __init__(self):
        Exception.__init__(self)
        self.message = "Invalid password."
        self.code = 400

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.message

    @property
    def http_response(self):
        return make_response(jsonify(message=self.message), self.code)
