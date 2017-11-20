from passlib.hash import pbkdf2_sha256

PASSWORD = "password"


def encrypt(content):
    content[PASSWORD] = PasswordHelper.encrypt(content[PASSWORD])
    return content


def valid_password(password, hash):
    return PasswordHelper.verify(password, hash)


class PasswordHelper:
    @staticmethod
    def encrypt(password):
        return pbkdf2_sha256.hash(password)

    @staticmethod
    def verify(password, hash):
        return pbkdf2_sha256.verify(password, hash)
