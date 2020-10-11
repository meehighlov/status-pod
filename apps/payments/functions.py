import sqlite3

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


def get_all_payments_data(update, context):  # ONLY FOR DEBUGGING! could be a lot of data to return
    connection = sqlite3.connect(config.DB_NAME)
    cursor = connection.cursor()
    cursor.execute('''select * from payments;''')
    data = cursor.fetchall()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'{data}'
    )
