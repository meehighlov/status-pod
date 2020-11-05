"""
    read tasks from db and then create schedules

    WARNING: hardcoded notification
    TODO make read from file
    TODO make it changeable from interface
"""
from core import config
from core.utils import strip_none_params, get_seconds_by_days


def repeating_notification(job_queue, *args):
    job_queue.run_repeating(*args)


def run_once_notification(job_queue, *args):
    job_queue.run_once(*args)


notifications = {
    'rent': {
        'message': 'Rent time!',
        'schedule_function': repeating_notification,
        'seconds': get_seconds_by_days(days=28),
        'start_from_seconds': 0
    },
    'additional_rent': {
        'message': 'Check mail box downstairs',
        'schedule_function': repeating_notification,
        'seconds': get_seconds_by_days(days=14),
        'start_from_seconds': 1
    },
    'phone': {
        'message': 'Are you still in connection? Check balance on the phone',
        'schedule_function': repeating_notification,
        'seconds': get_seconds_by_days(days=21),
        'start_from_seconds': 2
    },
    'internet': {
        'message': 'Check the internet access',
        'schedule_function': repeating_notification,
        'seconds': get_seconds_by_days(days=21),
        'start_from_seconds': 3
    },
    'haircut': {
        'message': 'Do you need refresh your haircut?',
        'schedule_function': repeating_notification,
        'seconds': get_seconds_by_days(days=21),
        'start_from_seconds': 4
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
