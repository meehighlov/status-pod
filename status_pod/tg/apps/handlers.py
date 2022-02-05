from telegram.ext import CommandHandler
from status_pod.tg.apps.insta_subs.handlers import get_subs_info


def start_command(update, context):
    username = update.message.chat.username  # TODO use it for login
    context.bot.send_message(chat_id=update.effective_chat.id, text="That's where the fun begins")


def check_responsive(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='ready')


handlers = [
    CommandHandler('start', start_command),  # handling start command
    CommandHandler('unfollow', get_subs_info),
    CommandHandler('check', check_responsive),
]
