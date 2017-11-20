import unittest

from utils.convert_string import StringConverter


class TestCamelCaseToSnakeCase(unittest.TestCase):
    def test_camel_case_to_snake_case(self):
        """
            Asserts if converts a camelCase name to snakeCase
            correctly
        """
        value = 'fooBar'
        expected = 'foo_bar'
        actual = StringConverter.camel_case_to_snake_case(value)
        self.assertEqual(expected, actual)
