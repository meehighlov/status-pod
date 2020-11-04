"""
    read tasks from db and then create schedules

    WARNING: hardcoded notification
    TODO make read from file
    TODO make it changeable from interface
"""
from core import config
from core.utils import strip_none_params


def repeating_notification(job_queue, *args):
    job_queue.run_repeating(*args)


def run_once_notification(job_queue, *args):
    job_queue.run_once(*args)



notifications = {
    'rent': {
        'message': 'Rent time!',
        'schedule_function': repeating_notification,
        'seconds': 5,
        'start_from_seconds': 5
    }
}


def notification_fabric(message):

    def notification(context):
        context.bot.send_message(
            chat_id=config.MY_CHAT_ID,
            text=message
        )

    return notification


def create_notifications(job_queue):
    for _, data in notifications.items():
        launch = data['schedule_function']
        notification = notification_fabric(data['message'])
        launch(
            job_queue,
            *strip_none_params(
                notification,
                data.get('seconds'),
                data.get('start_from_seconds')
            )
        )
