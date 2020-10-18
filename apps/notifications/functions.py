def notification_fabric(*args, **kwargs):

    def notification(context):
        chat_id = kwargs['chat_id']
        message = kwargs['message']
        context.bot.send_message(chat_id=chat_id, text=message)

    return notification
