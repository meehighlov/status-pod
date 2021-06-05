from core.config import config
from apps.handlers import handlers
from telegram.ext import Updater


# TODO Error handling

# TODO unit tests
# TODO fix Incorrect number of bindings supplied. The current statement uses 1, and there are 10 supplied.
# when use pi command


def init_bot():
    updater = Updater(token=config.TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # TODO AUTH!

    for handler in handlers:
        dispatcher.add_handler(handler)

    # TODO use webhook
    updater.start_polling()
    updater.idle()
