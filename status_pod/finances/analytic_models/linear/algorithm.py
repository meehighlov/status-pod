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
from status_pod.finances.analytic_models.utils import process_number_from_table


class BaseAlgorithm:

    _date_format = '%d.%m.%Y'  # формат даты в таблице

    def __init__(self, *args, **kwargs):
        self.data = kwargs['data']  # обязательный аргумент
        self._meta = self._process_meta(kwargs.get('meta'))
        self._analytics_result = None

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
    def _check_rest_for_date(self, date: str, budget: float):
        pass

    def _get_info_from_data(self, index: str, column: str = None, allow_multiple_results=False):
        try:
            data = self.data[index]
            if isinstance(data, list):
                # нашли несколько результатов - индекс неуникален в столбце
                if allow_multiple_results:
                    if column:
                        self._check_column(column)
                        return [datum[column] for datum in data]
                    return data
                raise SpendingAnalyticsAlgorithmError(f'multiple results found by index {index}')
            if column:
                self._check_column(column)
                return data[column]
            return data
        except KeyError:
            raise SpendingAnalyticsAlgorithmError(f'data was not build for index {index}')


class Linear(BaseAlgorithm):
    def get_value_by_date_and_category(self, date: str, category: str):
        self._check_column(category)
        return self.data[date][category]

    def get_all_info_by_date(self, date: str):
        return self._get_info_from_data(index=date)

    def _build_analysis(self):
        return self.data

    def _check_rest_for_date(self, date: str, desired_budget: float):
        """
        :param date: дата для которой мы проверяем бюджет
        :param desired_budget: сумма денег, в которую мы хотим попасть на дату date
        :return:
        """
        date_ = datetime.strptime(date, self._date_format)
        today_ = datetime.today()
        if date_ <= today_:
            raise SpendingAnalyticsAlgorithmError(
                'Why you cant analyse it by your own?'
                ' Specified date have to be > than today'
            )

        today = today_.strftime(self._date_format)
        data = self._get_info_from_data(index=today)


    def spend_by_period_by_category(self, date_begin: str, date_end: str, category: str):
        self._check_column(category)
        pass

    def spend_by_period_by_all_categories(self, date_begin: str, date_end: str):
        pass
