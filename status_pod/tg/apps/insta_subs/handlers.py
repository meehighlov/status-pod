from status_pod.instagram.main import subs


def get_subs_info(update, context):
    results = subs()

    command_to_detail = {
        'unfollow': 'not follow me back'
    }

    # command = context.args[0]
    report_detail = command_to_detail['unfollow']

    message = (
        f'{report_detail}:\n'
        f'{results[report_detail]}'
    )

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message
    )
