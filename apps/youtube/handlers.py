from apps.youtube.functions import get_audio_by_url_from_youtube


def get_audio_by_url(update, context):
    url = context.args[0]  # TODO validate
    try:
        audio = get_audio_by_url_from_youtube(url)
    except Exception:
        context.bot.send_message(chat_id=update.effective_chat.id, text='unable to download file')
        return
    context.bot.send_audio(chat_id=update.effective_chat.id, audio=audio)
