import unittest

from authentication.password import PasswordHelper, encrypt


class TestEncryptPassword(unittest.TestCase):
    def test_encrypt_password(self):
        """
            Asserts if encrypted password doesn't contain
            actual given password
        """
        password = "123456"
        actual = PasswordHelper.encrypt(password)

        self.assertTrue(password not in actual)

    def test_encrypt(self):
        """
            Asserts if password key of content is
            encrypted
        """
        password = "pip"
        content = {
            "name": "Eryk",
            "password": "pip"
        }
        actual = encrypt(content)

        self.assertEqual(content["name"], actual["name"])
        self.assertTrue(password not in actual["password"])

    def test_verify(self):
        """
            Asserts if password key of content is
            encrypted
        """
        password = "123456"
        hash = PasswordHelper.encrypt(password)

        self.assertTrue(PasswordHelper.verify(password, hash))
