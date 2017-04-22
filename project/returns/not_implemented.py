from project.returns import HTTP_NOT_IMPLEMENTED


def not_implemented():
    return {
               "message": "This method has not been implemented yet",
               "code": HTTP_NOT_IMPLEMENTED
           }, HTTP_NOT_IMPLEMENTED
