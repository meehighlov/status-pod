def strip_none_params(*args):
    return [param for param in args if param is not None]
