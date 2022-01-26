from status_pod.instagram.main import subs


def get_subs_info(update, context):
    message = None
    try:
        results = subs()
    except Exception as e:
        message = f'insta fault with exception: {e}'

    command_to_detail = {
        'unfollow': 'not follow me back'
    }

    # command = context.args[0]
    report_detail = command_to_detail['unfollow']

    message = message or (
        f'{report_detail}:\n'
        f'{results[report_detail]}'
    )

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message
    )
