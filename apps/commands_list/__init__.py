commands = {
    'p': 'saves payment, format: /p item cost',
    'pi': 'retrieves all payments by period, format: /pi Y.mm.dd',
    'ps': 'retrieves all payments by date, format: /ps [t|w|m|y]',
    # 'pa': 'retrieves all payments in db, format: /pa'  ONLY FOR DEBUG

    'ci': 'commands info, format /ci [command]'
}


def get_list_of_commands(update, context):
    command = context.args or None

    message = '\n'.join([
        f'{command}: {description}'
        for command, description in commands.items()
    ])

    if command is None:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=message
        )
        return

    command_info = commands.get(command[0])
    if not command_info:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Unknown command, use /ci to see list of commands'
        )
        return

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=command_info
    )
