from project.returns import HTTP_BAD_REQUEST
from utils.scalarize_arguments import scalarize


def must_be_integer():
    return {
                "message": "Valor inserido deve ser um inteiro.",
                "code": HTTP_BAD_REQUEST
           }, HTTP_BAD_REQUEST


def missing_fields(*args):
    return {
                "message": "Os campos (%s) devem ser enviados." % ', '.join(str(arg) for arg in scalarize(args)),
                "code": HTTP_BAD_REQUEST
           }, HTTP_BAD_REQUEST


def invalid_fields(*args):
    return {
                "message": "Não é possível modificar o(s) campo(s): %s." % ', '.join(str(arg) for arg in scalarize(args)),
                "code": HTTP_BAD_REQUEST
           }, HTTP_BAD_REQUEST
