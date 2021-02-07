from contextlib import suppress
from datetime import datetime

from status_pod.finances.analytic_models.utils import process_number_from_table


class TableRow:

    _datetime_format = '%d.%m.%Y'

    def __init__(self, attrs: dict):
        self.__attrs = attrs

    @property
    def attrs(self):
        return self.__attrs

    def __contains__(self, item):
        # TODO case insensitive
        return item in self.__attrs

    def __getitem__(self, item):
        # TODO case insensitive
        # TODO постоянно такое дергать - может быть накладно, надо оптимизировать
        return self.__process_value(self.__attrs[item])

    def __setitem__(self, key, value):
        # TODO case insensitive
        self.__attrs[key] = value

    def __str__(self):
        return str(self.__attrs)

    def to_datetime(self, value: str):
        return datetime.strptime(value, self._datetime_format)

    def to_float(self, value: str):
        return process_number_from_table(value)

    def __process_value(self, value: str):
        for f in [self.to_datetime, self.to_float]:
            with suppress(TypeError, ValueError):
                value = f(value)
        return value
