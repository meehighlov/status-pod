"""
    custom creating tasks (from messages)
"""


def notification_fabric(*args, **kwargs):

    def notification(context):
        chat_id = kwargs['chat_id']
        message = kwargs['message']
        context.bot.send_message(chat_id=chat_id, text=message)

    return notification


def add_notification_from_message(update, context):
    # format: /na notification text date hh:mm
    # day -> dd.mm

    notification_params = context.args

    try:
        day_, time_ = notification_params[-2:]

    except (ValueError, IndexError):
        pass

    # message = notification_params.text
    # timer_options = notification_params.schedule
    # notification = notification_fabric(
    #     chat_id=config.chat_id
    #     message=message
    # )
    # context.job_queue.run_repeating(
    #     notification,
    #     interval=timer_options,
    #     first=timer_options
    # )
