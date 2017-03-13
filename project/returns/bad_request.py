from project.returns import HTTP_BAD_REQUEST


def must_be_integer():
    return {
               "message": "Valor inserido deve ser um inteiro"
           }, HTTP_BAD_REQUEST


def missing_fields(*args):
    return {
               "message": "Os campos (%s) devem ser enviados" % ', '.join(str(arg) for arg in args)
           }, HTTP_BAD_REQUEST
