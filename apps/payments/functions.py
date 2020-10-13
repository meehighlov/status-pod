import sqlite3
import datetime

from core.config import config
from datetime import date


#TODO make decorators for work with db -> a lot of code repetitions
#TODO also add to decorator: checking type of update and context variables -
# is they instances of classes that we waiting for; or simply add type hinting


def save_payment(update, context):
    try:
        item, cost = context.args
        cost = float(cost)
    except ValueError:
        context.bot.send_message(chat_id=update.effective_chat.id, text='not saved')
        return
    connection = sqlite3.connect(config.DB_NAME)
    cursor = connection.cursor()
    cursor.execute(
        '''insert into payments values (?, ?, ?);''', (
            item,
            cost,
            date.today().strftime("%Y.%m.%d")
        )
    )
    connection.commit()
    connection.close()
    context.bot.send_message(chat_id=update.effective_chat.id, text='saved')


def get_all_payments_by_date(update, context):
    date = context.args
    # TODO check date format
    if not date:
        pass  # TODO

    # TODO make decorator for that purpose
    connection = sqlite3.connect(config.DB_NAME)  # <- takeout to decorator
    cursor = connection.cursor()  # <- takeout to decorator

    cursor.execute('''select * from payments where date = ?;''', date)

    data = cursor.fetchall()  # <- takeout to decorator ?

    connection.close()  # <- takeout to decorator

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


def get_payments_stat_for_period(update, context):
    # period format:
    # w - last week (today inclusive)
    # m - last month
    # y - last year

    period = context.args  # TODO validation

    letter_to_date_map = {
        'w': (date.today() - datetime.timedelta(days=7), date.today()),
        'm': (date.today() - datetime.timedelta(days=30), date.today()),  # what about february?
        'y': (date.today() - datetime.timedelta(days=365), date.today())  # what about 366?
    }

    connection = sqlite3.connect(config.DB_NAME)
    cursor = connection.cursor()

    time_format = '%Y.%m.%d'

    a, b = letter_to_date_map[period[0]]
    a, b = a.strftime(time_format), b.strftime(time_format)

    # sqlite not able to work with datetime
    # comparison only in strings -> y.m.d format works for that well
    cursor.execute(
        '''
        select * from payments where
            ? <= date and date <= ?
        ''',
        (a, b)
    )

    data = cursor.fetchall()
    connection.close()

    #TODO prepare output!
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'{data}'
    )


def get_all_payments_data(update, context):  # ONLY FOR DEBUGGING! could be a lot of data to return
    connection = sqlite3.connect(config.DB_NAME)
    cursor = connection.cursor()
    cursor.execute('''select * from payments;''')
    data = cursor.fetchall()
    connection.close()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'{data}'
    )
