from returns import HTTP_UNAUTHORIZED


def unauthorized():
    return {
               "message": "You are not authorized to do this!"
           }, HTTP_UNAUTHORIZED
