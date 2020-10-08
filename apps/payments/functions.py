import sqlite3

from core.config import config


def payments(update, context):
    text = update.message.text
    try:
        item, cost = text.split()
        cost = float(cost)
    except ValueError:
        context.bot.send_message(chat_id=update.effective_chat.id, text='not saved')
        return
    connection = sqlite3.connect(config.DB_NAME)
    cursor = connection.cursor()
    cursor.execute('''insert into payments values (?, ?, ?)''', (item, cost, 'today'))
    connection.commit()
    connection.close()
    context.bot.send_message(chat_id=update.effective_chat.id, text='saved')
