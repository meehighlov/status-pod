import os
import dotenv

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

dotenv.load_dotenv()

token = os.getenv('TOKEN')

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


def intro(update, context):
    print('into intro')
    context.bot.send_message(chat_id=update.effective_chat.id, text="That's where the fun begins")


def reflector(update, context):
    print(f'chat id {update.effective_chat.id}')
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)




start_handler = CommandHandler('start', intro)
message_handler = MessageHandler(Filters.text & (~Filters.command), reflector)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)
updater.start_polling()
updater.idle()
