def strip_none_params(*args):
    return [param for param in args if param is not None]


def get_seconds_by_days(days):
    minute = 60
    hour = minute * 60
    day = hour * 24
    return day * days
