from apps.handlers import handlers
from telegram.ext import Updater, CommandHandler
from core.config import config


updater = Updater(token=config.TOKEN, use_context=True)
dispatcher = updater.dispatcher


# TODO AUTH!


def start_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="That's where the fun begins")


def register_handlers(handlers, dispatcher):
    for handler in handlers:
        dispatcher.add_handler(handler)


handlers_ = [
    CommandHandler('start', start_command),
    *handlers
]

register_handlers(handlers_, dispatcher)
updater.start_polling()
updater.idle()
