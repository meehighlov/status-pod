"""
    custom creating tasks (from messages)
"""


def notification_fabric(*args, **kwargs):

    def notification(context):
        chat_id = kwargs['chat_id']
        message = kwargs['message']
        context.bot.send_message(chat_id=chat_id, text=message)

    return notification


"""
    sample

    def message_handler(update, context):
        notification_params =  context.args
        message = notification_params.text
        timer_options = notification_params.schedule
        notification = notification_fabric(
            chat_id=config.chat_id
            message=message
        )
        context.job_queue.run_repeating(
            notification,
            interval=timer_options,
            first=timer_options
        )
"""
