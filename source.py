import os
import sqlite3

import dotenv
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from apps.persistant.db import db

dotenv.load_dotenv()

token = os.getenv('TOKEN')

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
# queue = updater.job_queue


def intro(update, context):
    print('into intro')
    context.bot.send_message(chat_id=update.effective_chat.id, text="That's where the fun begins")


def reflector(update, context):
    db.cursor.execute(''' select * from payments ''')
    r = db.cursor.fetchall()
    print(f'db data {r}')
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def payments(update, context):
    text = update.message.text
    try:
        item, cost = text.split()
        cost = float(cost)
    except ValueError:
        context.bot.send_message(chat_id=update.effective_chat.id, text='not saved')
        return
    connection = sqlite3.connect('temporary.persistant')
    cursor = connection.cursor()
    cursor.execute('''select * from payments;''')
    r = cursor.fetchall()
    print(f'db data {r}')
    cursor.execute('''insert into payments values (?, ?, ?)''', (item, cost, 'today'))
    connection.commit()
    connection.close()
    context.bot.send_message(chat_id=update.effective_chat.id, text='saved')


start_handler = CommandHandler('start', intro)
payments_handler = MessageHandler(Filters.text & (~Filters.command), payments)
# message_handler = MessageHandler(Filters.text & (~Filters.command), reflector)

# job_minute = queue.run_repeating(callback, interval=10, first=0)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(payments_handler)
updater.start_polling()
updater.idle()
