import datetime

from apps.persistant.db import db_connection
from datetime import date


#TODO make decorators for work with db -> a lot of code repetitions
#TODO also add to decorator: checking type of update and context variables -
# is they instances of classes that we waiting for; or simply add type hinting


@db_connection
def save_payment(update, context, db):
    try:
        item, cost = context.args
        cost = float(cost)
    except ValueError:
        context.bot.send_message(chat_id=update.effective_chat.id, text='not saved')
        return
    db.cursor.execute(
        '''insert into payments values (?, ?, ?);''', (
            item,
            cost,
            date.today().strftime("%Y.%m.%d")
        )
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text='saved')


@db_connection
def get_all_payments_by_date(update, context, db):
    date = context.args
    # TODO check date format
    if not date:
        pass  # TODO

    # TODO make decorator for that purpose

    db.cursor.execute('''select * from payments where date = ?;''', date)
    data = db.cursor.fetchall()

    # TODO prepare output!
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'{data}'
    )


def set_amount_of_money_for_spending_per_day(update, context):
    # setting amount of money is possible
    # if at the moment of setting there is no payments at the moment
    # otherwise set is not allowed - show message:
    # 'you already spent money today - set is not possible'

    # am i realy need it?
    pass


@db_connection
def get_payments_stat_for_period(update, context, db):
    # period format:
    # t - today
    # w - last week (today inclusive)
    # m - last month
    # y - last year

    period = context.args  # TODO validation

    letter_to_date_map = {
        't': (date.today(), date.today()),
        'w': (date.today() - datetime.timedelta(days=7), date.today()),
        'm': (date.today() - datetime.timedelta(days=30), date.today()),  # what about february?
        'y': (date.today() - datetime.timedelta(days=365), date.today())  # what about 366?
    }

    time_format = '%Y.%m.%d'

    a, b = letter_to_date_map[period[0]]
    a, b = a.strftime(time_format), b.strftime(time_format)

    # sqlite not able to work with datetime
    # comparison only in strings -> y.m.d format works for that well
    db.cursor.execute(
        '''
        select * from payments where
            ? <= date and date <= ?
        ''',
        (a, b)
    )

    data = db.cursor.fetchall()

    #TODO prepare output!
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'{data}'
    )


@db_connection
def get_all_payments_data(update, context, db):  # ONLY FOR DEBUGGING! could be a lot of data to return
    db.cursor.execute('''select * from payments;''')
    data = db.cursor.fetchall()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'{data}'
    )
