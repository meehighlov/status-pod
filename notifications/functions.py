"""
    read tasks from db and then create schedules

    WARNING: hardcoded notification
    TODO make it changeable from interface
"""
from core import config



def repeating_notification(job_queue, *args):
    job_queue.run_repeating(*args)


def run_once_notification(job_queue, *args):
    job_queue.run_once(*args)



notification_messages_list = {
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
    for _, data in notification_messages_list.items():
        launch = data['schedule_function']
        notification = notification_fabric(data['message'])
        launch(
            job_queue,
            notification,
            data['seconds'],
            data.get('start_from_seconds')
        )
