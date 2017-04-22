from returns import HTTP_STATUS_OK


def deactivated():
    return {
               "message": "Desativado com sucesso."
           }, HTTP_STATUS_OK


def modified():
    return {
               "message": "Alterado com sucesso."
           }, HTTP_STATUS_OK


def inserted():
    return {
               "message": "Inserido com sucesso."
           }, HTTP_STATUS_OK
