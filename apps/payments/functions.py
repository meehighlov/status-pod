import sqlite3
import datetime

from core.config import config
from datetime import date


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
            date.today().strftime("%d.%m.%Y")
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
    connection = sqlite3.connect(config.DB_NAME)
    cursor = connection.cursor()
    cursor.execute('''select * from payments where date = ?;''', date)
    data = cursor.fetchall()
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

    for period_d in letter_to_date_map.values():
        for date_ in period_d:
            date_.strftime('%d.%m.Y')

    connection = sqlite3.connect(config.DB_NAME)
    cursor = connection.cursor()

    a, b = letter_to_date_map[period[0]]

    # it is not works like that (
    # add datetime support to db for table payments
    cursor.execute('''select * from payments where date >= ? and date < ?;''', (a, b))

    data = cursor.fetchall()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'{data}'
    )


def get_all_payments_data(update, context):  # ONLY FOR DEBUGGING! could be a lot of data to return
    connection = sqlite3.connect(config.DB_NAME)
    cursor = connection.cursor()
    cursor.execute('''select * from payments;''')
    data = cursor.fetchall()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'{data}'
    )
