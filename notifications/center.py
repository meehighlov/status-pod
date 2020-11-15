"""
    read tasks from db and then create schedules

    WARNING: hardcoded notification
    TODO make read from file
    TODO make it changeable from interface
"""
import datetime

from core import config
from core.utils import strip_none_params, get_seconds_by_days



def repeating_notification(job_queue, *args):
    job_queue.run_repeating(*args)


def run_once_notification(job_queue, *args):
    job_queue.run_once(*args)


notifications = {
    'rent': {
        'message': 'Rent time!',
        'repeat_times': 3,
        'schedule_function': repeating_notification,
        'interval': datetime.timedelta(seconds=2),
        'first': datetime.datetime.strptime('15.11.2020', '%d.%m.%Y')
    },
    # 'additional_rent': {
    #     'message': 'Check mail box downstairs',
    #     'schedule_function': repeating_notification,
    #     'interval': get_seconds_by_days(days=14),
    #     'first': 1
    # },
    # 'phone': {
    #     'message': 'Are you still in connection? Check balance on the phone',
    #     'schedule_function': repeating_notification,
    #     'interval': get_seconds_by_days(days=21),
    #     'first': 2
    # },
    # 'internet': {
    #     'message': 'Check the internet access',
    #     'schedule_function': repeating_notification,
    #     'interval': get_seconds_by_days(days=21),
    #     'first': 3
    # },
    # 'haircut': {
    #     'message': 'Do you need refresh your haircut?',
    #     'schedule_function': repeating_notification,
    #     'interval': get_seconds_by_days(days=21),
    #     'first': 4
    # }
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
                data.get('interval'),
                data.get('first')
            )
        )


tasks = {
    'rent': {
        'message': 'Rent time!',
        'datetime': '',
    }
}



def periodical_task_checker():
    pass

