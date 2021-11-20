from telegram.ext import CommandHandler

from status_pod.tg.apps.commands_list import get_list_of_commands
from status_pod.tg.apps.youtube.handlers import get_audio_by_url


def start_command(update, context):
    username = update.message.chat.username  # TODO use it for login
    context.bot.send_message(chat_id=update.effective_chat.id, text="That's where the fun begins")


def hey(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Привет, Оля')


handlers = [
    CommandHandler('start', start_command),  # handling start command
    CommandHandler('ci', get_list_of_commands),
    CommandHandler('ymp3', get_audio_by_url),
    CommandHandler('hey', hey),
]
