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


def check_triggers():
    pass
