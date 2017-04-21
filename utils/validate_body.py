def parse_columns(data, columns):
    for column in columns:
        if column not in data:
            data.update({column: None})
    return data


def validate_body(data, required_columns, columns):
    missing_fields = list()
    for required_column in required_columns:
        if required_column not in data:
            missing_fields.append(required_column)

    if missing_fields != list():
        error = KeyError("Fields (%s) were not sent." % ', '.join(str(arg) for arg in missing_fields))
        error.fields = missing_fields
        raise error
    else:
        return parse_columns(data, columns)
