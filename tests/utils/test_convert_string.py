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
        actual = StringConverter().camel_case_to_snake_case(value)
        self.assertEqual(expected, actual)

    def test_camel_case_to_snake_case_list(self):
        """
            Asserts if converts all items of a list
            from camelCase to snakeCase correctly
        """
        items = [
            'fooBar',
            'pipTchu',
            'erykWho'
        ]
        expected = [
            'foo_bar',
            'pip_tchu',
            'eryk_who'
        ]
        actual = StringConverter().camel_case_to_snake_case(items)
        self.assertEqual(expected, actual)

    def test_camel_case_to_snake_case_dict(self):
        """
            Asserts if converts all keys of a dict
            from camelCase to snakeCase correctly
        """
        my_dict = {
            'fooBar': 'a',
            'pipTchu': 'b',
            'erykWho': 'c'
        }
        expected = {
            'foo_bar': 'a',
            'pip_tchu': 'b',
            'eryk_who': 'c'
        }
        actual = StringConverter().camel_case_to_snake_case(my_dict)
        self.assertEqual(expected, actual)

    def test_camel_case_to_snake_case_nested_dict(self):
        """
            Asserts if converts all keys of a nested dict
            from camelCase to snakeCase correctly
        """
        my_dict = {
            'fooBar': {
                'barFoo': 1,
            },
            'pipTchu': 'b',
            'erykWho': 'c'
        }
        expected = {
            'foo_bar': {
                'bar_foo': 1
            },
            'pip_tchu': 'b',
            'eryk_who': 'c'
        }
        actual = StringConverter().camel_case_to_snake_case(my_dict)
        self.assertEqual(expected, actual)


    def test_snake_case_to_camel_case(self):
        """
            Asserts if converts a snakeCase name to camelCase
            correctly
        """
        value = 'foo_bar'
        expected = 'fooBar'
        actual = StringConverter().snake_case_to_camel_case(value)
        self.assertEqual(expected, actual)

    def test_snake_case_to_camel_case_list(self):
        """
            Asserts if converts all the items of a list
            from snakeCase to camelCase correctly
        """
        items = ['foo_bar', 'pip_tchu', 'eryk_who']
        expected = ['fooBar', 'pipTchu', 'erykWho']
        actual = StringConverter().snake_case_to_camel_case(items)
        self.assertEqual(expected, actual)

    def test_snake_case_to_camel_case_dict(self):
        """
            Asserts if converts all the keys from a dict
            from snakeCase to camelCase correctly
        """
        my_dict = {
            'foo_bar': 'a',
            'pip_tchu': 'b',
            'eryk_who': 'c'
        }
        expected = {
            'fooBar': 'a',
            'pipTchu': 'b',
            'erykWho': 'c'
        }
        actual = StringConverter().snake_case_to_camel_case(my_dict)
        self.assertEqual(expected, actual)

    def test_snake_case_to_camel_case_nested_dict(self):
        """
            Asserts if converts all the keys from a nested dict
            from snakeCase to camelCase correctly
        """
        my_dict = {
            'foo_bar': {
                'bar_foo': 2
            },
            'pip_tchu': 'b',
            'eryk_who': 'c'
        }
        expected = {
            'fooBar': {
                'barFoo': 2
            },
            'pipTchu': 'b',
            'erykWho': 'c'
        }
        actual = StringConverter().snake_case_to_camel_case(my_dict)
        self.assertEqual(expected, actual)
