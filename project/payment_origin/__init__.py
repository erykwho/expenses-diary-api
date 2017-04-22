import flask_restful as restful
from flask import Blueprint  # pragma: no cover

from project.payment_origin.payment_origins import PaymentOrigins, PaymentOrigin

payment_origin = Blueprint(
    'payment_origin', __name__,
)

api = restful.Api()
api.init_app(payment_origin)

api.add_resource(PaymentOrigins, '/v1/payment-origins')
api.add_resource(PaymentOrigin, '/v1/payment-origins/<int:id>')
