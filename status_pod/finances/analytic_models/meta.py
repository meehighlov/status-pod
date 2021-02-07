"""
    будем ассоциировать таблицу в экселе с дата классом
    (возможно в дальнейшем и с таблицей в БД)
"""
from functools import partial
from status_pod.finances.analytic_models.utils import process_number_from_table, string_to_datetime


class TableRow:

    _datetime_format = '%d.%m.%Y'

    @property
    def __type_funcs(self):
        return [
            process_number_from_table,
            partial(string_to_datetime, fmt=self._datetime_format),
            str
        ]

    def __init__(self, attrs: dict):
        self.__attrs = attrs

    def __getattribute__(self, item):
        return self.__attrs.get(item)

    def __setattr__(self, key, value):
        if key not in self.__attrs:
            return
        self.__attrs[key] = value

    def __getitem__(self, item):
        return self.__attrs.get(item)

    def process_value(self, attr):
        value = self[attr]
        try:
            value_ = value
            for type_f in self._type_funcs:
                value_ = type_f(value)
            return value_
        except (ValueError, TypeError):
            pass
