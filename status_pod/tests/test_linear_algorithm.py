from functools import reduce


def sample(income, expense, days_amount, rest):
    funcs = [lambda r: r + income - expense] * days_amount
    return reduce(lambda i, f: f(i), funcs, rest)


def test_linear_algorithm_rest_counting():
    """
    вроде бы все верно, но выглядит достаточно наивно:
    преположим, что доход на сегодня
    не повторится завтра в том же объеме (например получили зп)
    следовательно, остаток всегда будет положтельный при тратах < дохода за день

    это необходимо учесть и доработать алгоритм:
    например, при расчете на каждый следующий день, не учитывать новые денежные поступления

    после того, как этот алгоритм будет реализован - следующий шаг, это
    предложения о том, как можно уложиться в желаемый бюджет,
    либо не попасть в минус на конкретную дату
    """
    today_data = {
        'income': 100,
        'expense': 50,
        'rest': 50
    }
    days_to_desired_date = 2
    r = sample(**today_data, days_amount=days_to_desired_date)
    assert r == 150
