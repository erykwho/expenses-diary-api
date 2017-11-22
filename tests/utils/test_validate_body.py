import unittest

from utils.validate_body import parse_columns, validate_update_columns


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
            'fooBar': 1,
            'pip': 2,
            'schuMan': None
        }

        actual = parse_columns(data, columns)
        self.assertEqual(expected, actual)

    def test_validate_update_columns(self):
        data = {
            'a': 1,
            'b': 2
        }
        columns = [
            'a',
            'b'
        ]
        expected = data
        actual = validate_update_columns(data, columns)
        self.assertEqual(expected, actual)

    def test_validate_update_columns_should_convert_case(self):
        data = {
            'columnA': 1,
            'columnB': 2
        }
        columns = [
            'columnA',
            'columnB'
        ]
        expected = {
            'column_a': 1,
            'column_b': 2
        }
        actual = validate_update_columns(data, columns)
        self.assertEqual(expected, actual)
