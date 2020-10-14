from telegram.ext import CommandHandler
from apps.payments.functions import (
    save_payment,
    get_all_payments_by_date,
    get_all_payments_data,
    get_payments_stat_for_period
)


def start_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="That's where the fun begins")


handlers = [
    CommandHandler('start', start_command),  # handling start command
    CommandHandler('p', save_payment),  # p - payment
    CommandHandler('pi', get_all_payments_by_date),  # pi - payment info
    CommandHandler('pa', get_all_payments_data),  # pa - payments all
    CommandHandler('ps', get_payments_stat_for_period)  # ps - payments stat
]
