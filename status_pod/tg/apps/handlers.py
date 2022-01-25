from telegram.ext import CommandHandler

from status_pod.tg.apps.commands_list import get_list_of_commands
from status_pod.tg.apps.insta_subs.handlers import get_subs_info


def start_command(update, context):
    username = update.message.chat.username  # TODO use it for login
    context.bot.send_message(chat_id=update.effective_chat.id, text="That's where the fun begins")


handlers = [
    CommandHandler('start', start_command),  # handling start command
    CommandHandler('ci', get_list_of_commands),
    CommandHandler('unfollow', get_subs_info)
]
