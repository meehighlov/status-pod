from core.config import config
from apps.handlers import handlers
from telegram.ext import Updater


def init_bot():
    updater = Updater(token=config.TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # TODO AUTH!

    for handler in handlers:
        dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()
