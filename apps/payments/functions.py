import sqlite3

from core.config import config


def save_payment(update, context):
    try:
        item, cost = context.args
        cost = float(cost)
    except ValueError:
        context.bot.send_message(chat_id=update.effective_chat.id, text='not saved')
        return
    connection = sqlite3.connect(config.DB_NAME)
    cursor = connection.cursor()
    cursor.execute('''insert into payments values (?, ?, ?);''', (item, cost, 'today'))
    connection.commit()
    connection.close()
    context.bot.send_message(chat_id=update.effective_chat.id, text='saved')


def get_all_payments_by_date(update, context):
    try:
        date = context.args
    except ValueError:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='syntax error'
        )
        return
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
