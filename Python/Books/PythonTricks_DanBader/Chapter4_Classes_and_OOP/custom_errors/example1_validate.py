def validate(name):
    if len(name) < 10:
        raise ValueError


validate('joe')
