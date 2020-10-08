from telegram.ext import MessageHandler, Filters
from apps.payments.functions import payments


handlers = [
    MessageHandler(Filters.text & (~Filters.command), payments)
]
