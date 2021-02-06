"""
    будем ассоциировать таблицу в экселе с дата классом
    (возможно в дальнейшем и с таблицей в БД)
"""

from dataclasses import dataclass, field


@dataclass
class ExpenseIncome:
    day: str
    date: str
    rest: str
    income: str
    expense_total: str
    house_or_clothes: str
    food: str
    health_and_beauty: str
    transport: str
    entertainment_travel: str
    mishel: str
    gifts: str
    olka: str
    credits_banks_loans: str
    cash: str
    investments: str
