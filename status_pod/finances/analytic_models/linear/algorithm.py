"""
    standard discussed algorithm

    definitions:

    category = type of spending
    total_spent = sum of spent money amount on each category during the day
    income = incoming money amount (defines by user)
    rest = yesterday.rest + yesterday.income - yesterday.total_spent (first rest defines by user)
    day = as usual
    date = as usual

    analysis goals

    main (still have questions):

    TODO - ask about it
    to tell the user that with the same spending user still in his budget (or not) for specified date (?)

    advantage:

    1 highlight when rest < specified_minimum
    2 highlight when any category drops rest down to specified_minimum
"""
from abc import abstractmethod
from datetime import datetime
from status_pod.app.exceptions import SpendingAnalyticsAlgorithmError
from functools import reduce


class BaseAlgorithm:

    _date_format = '%d.%m.%Y'  # формат даты в таблице

    def __init__(self, *args, **kwargs):
        self.data = kwargs['data']  # обязательный аргумент
        self._meta = self._process_meta(kwargs.get('meta'))
        self._analytics_result = None
        self._main_columns = self._process_main_columns(kwargs.get('main_columns', None))

    def _process_meta(self, meta):
        """
        метаинформация для текущего представления excel таблицы - заголовки (шапка таблицы)
        проверяем, что заголовки переданы в виде: List[List[Str]], либо List[Str]
        преобразововываем к виду: Set[Str]
        """
        if not meta:
            raise SpendingAnalyticsAlgorithmError('meta data is missing')

        if isinstance(meta, (list, set)) and all([isinstance(i, str) for i in meta]):
            return set(meta)

        try:
            meta = {*meta[0], *meta[1]}
        except (TypeError, IndexError):
            raise SpendingAnalyticsAlgorithmError('meta data has incorrect format')

        return meta

    def _process_main_columns(self, main_columns, use_dangerous=True):
        """
        главные столбцы - это столбцы, по которым мы делаем расчет

        сейчас это: остаток, расход, доход

        :param use_dangerous - дефолтный вариант, когда главные столбцы хардкодятся
        :return: dict
        """

        if isinstance(main_columns, dict):
            # передан маппинг - пологаем что он верный и пропускаем его
            return main_columns

        if callable(main_columns):
            processed = main_columns()
            if not isinstance(processed, dict):
                raise SpendingAnalyticsAlgorithmError(
                    f'error occurred during main columns processing, got result: {processed}'
                )
            return processed

        if not main_columns:
            if use_dangerous:
                return {
                    'expense': 'Расход тотал',
                    'income': 'Приход',
                    'rest': 'Остаток'
                }
            raise SpendingAnalyticsAlgorithmError(
                f'error occurred during main columns processing, '
                f'params conflict: use_dangerous = {use_dangerous},'
                f'main_columns = {main_columns}'
            )

    def get_analytics_results(self):
        if self._analytics_result:
            return self._analytics_result
        self._analytics_result = self._build_analysis()
        return self._analytics_result

    def _check_column(self, column):
        if column not in self._meta:
            raise SpendingAnalyticsAlgorithmError(f'column {column} not found in {self._meta}')

    @abstractmethod
    def _build_analysis(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_rest_for_date(self, date: str):
        pass

    def _get_info_from_data(self, index: str, column: str = None):
        """
        Будет работать толкьо в случае,
        если индекс строится для уникальных значений, например для даты
        :param index: индекс (имя столбца)
        :param column: имя столбца, по которому нужно достать данные, из полученного набора по индексу
        :return:
        """
        try:
            data = self.data[index]
            if column:
                self._check_column(column)
                return data[column]
            return data
        except KeyError:
            raise SpendingAnalyticsAlgorithmError(f'unknown column or index {column, index}')


class Linear(BaseAlgorithm):
    def get_value_by_date_and_category(self, date: str, category: str):
        self._check_column(category)
        return self.data[date][category]

    def get_all_info_by_date(self, date: str):
        return self._get_info_from_data(index=date)

    def _build_analysis(self):
        return self.data

    def get_rest_for_date(self, date: str) -> float:
        """
        :param date: дата для которой мы проверяем бюджет
        :return: actual_rest
        """
        date_ = datetime.strptime(date, self._date_format)
        today_ = datetime.today()
        if date_ <= today_:
            raise SpendingAnalyticsAlgorithmError(
                'Why you cant analyse it by your own?'
                ' Specified date has to be > than today'
            )

        today = today_.strftime(self._date_format)
        today_data = self._get_info_from_data(index=today)
        if today_data is None:
            raise SpendingAnalyticsAlgorithmError(f'Not found data for today: {today}')

        expense = today_data[self._main_columns['expense']]
        rest = today_data[self._main_columns['rest']]
        income = today_data[self._main_columns['income']]

        days_amount = (date_ - today_).days
        funcs = [lambda r: r + income - expense] * days_amount

        return reduce(lambda i, f: f(i), funcs, rest)

    def spend_in_period_by_category(self, date_begin: str, date_end: str, category: str):
        self._check_column(category)
        pass

    def spend_in_period_by_all_categories(self, date_begin: str, date_end: str):
        pass
