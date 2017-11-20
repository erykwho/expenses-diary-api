import unittest

from utils.validate_body import parse_columns


class TestParseColumns(unittest.TestCase):
    def test_parse_columns(self):
        """
            Asserts if parse columns correctly
            It should also convert keys to underscore case
        """

        data = {
            'fooBar': 1,
            'pip': 2
        }

        columns = ['fooBar', 'pip', 'schuMan']

        expected = {
            'foo_bar': 1,
            'pip': 2,
            'schu_man': None
        }

        actual = parse_columns(data, columns)
        self.assertEqual(expected, actual)
