from core.config import config
from apps.handlers import handlers
from telegram.ext import Updater

from notifications.center import create_notifications


# TODO Error handling


def init_bot():
    updater = Updater(token=config.TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # TODO AUTH!

    for handler in handlers:
        dispatcher.add_handler(handler)

    create_notifications(updater.job_queue)

    updater.start_polling()
    updater.idle()
