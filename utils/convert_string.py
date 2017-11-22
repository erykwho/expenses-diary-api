import re
from functools import wraps


def camel_case_to_snake_case_wrapper(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        new_args = (StringConverter().camel_case_to_snake_case(arg) for arg in args)
        return f(*new_args, **kwargs)

    return wrap


class StringConverter:
    def camel_case_to_snake_case(self, items):
        if isinstance(items, dict):
            return self._iter_filter(items, self._camel_case_to_snake_case)

        if isinstance(items, list):
            for i, item in enumerate(items):
                items[i] = self._camel_case_to_snake_case(item)

            return items

        return self._camel_case_to_snake_case(items)

    def _iter_filter(self, item, filter_function):
        if not isinstance(item, dict):
            return item

        new_items = {}
        for key, value in item.items():
            new_key = filter_function(key)
            new_value = self._iter_filter(value, filter_function)
            new_items[new_key] = new_value
        return new_items

    @staticmethod
    def _camel_case_to_snake_case(item):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', item)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def snake_case_to_camel_case(self, items):
        if isinstance(items, dict):
            new_items = self._iter_filter(items, self._snake_case_to_camel_case)
            return new_items

        if isinstance(items, list):
            for i, item in enumerate(items):
                items[i] = self._snake_case_to_camel_case(item)
            return items

        return self._snake_case_to_camel_case(items)

    @staticmethod
    def _snake_case_to_camel_case(item):
        components = item.split('_')
        # We capitalize the first letter of each component except the first one
        # with the 'title' method and join them together.
        return components[0] + "".join(x.title() for x in components[1:])
