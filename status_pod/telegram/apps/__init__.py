#TODO this is stub

command_to_function_map = {
    'calculate': lambda x: x,
}


def execute_command(command: str, **kwargs):
    try:
        handler = command_to_function_map[command]
    except KeyError:
        raise KeyError('Unknown command handler')

    return handler(**kwargs)
