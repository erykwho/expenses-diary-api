from returns import HTTP_INTERNAL_SERVER_ERROR


def unexpected_error():
    return {
               "message": "Um erro inesperado ocorreu."
           }, HTTP_INTERNAL_SERVER_ERROR
