def scalarize(args):
    fields = list()
    for arg in args:
        if isinstance(arg, list):
            for field in arg:
                fields.append(field)
        else:
            fields.append(arg)
    return fields
