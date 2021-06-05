from telegram.ext import CommandHandler

from apps.commands_list import get_list_of_commands


def start_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="That's where the fun begins")


handlers = [
    CommandHandler('start', start_command),  # handling start command
    CommandHandler('ci', get_list_of_commands)
]
