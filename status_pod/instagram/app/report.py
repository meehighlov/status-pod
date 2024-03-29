from datetime import datetime
from functools import partial

from status_pod.app.config import config
from status_pod.app.exceptions import AppError


def save_report_as_txt(path: str, report: dict):
    dashes = f"{('-' * 20)}\n"
    spaces = ' ' * 2
    with open(path, 'w') as f:
        f.write(f'report {datetime.today().ctime()}\n')
        f.write(f'triggered by {config.INSTAGRAM_LOGIN}\n')
        for topic, lines in report.items():
            f.write(dashes)
            f.write(f'{topic}:\n')
            f.write(dashes)
            for line in lines:
                f.write(f'{spaces}{line}\n')


def save_report(*, fmt='txt', **kwargs):
    """
    :param fmt: формат
    :param kwargs:
        :param path: куда сложить отчет
        :param report: данные отчета
    :return:
    """

    # временно фиксируем название файла, так как оно указывается в гитигнор
    assert kwargs['path'] == 'report.txt'

    handler = {
        'txt': partial(save_report_as_txt, **kwargs)
    }.get(fmt)

    if not handler:
        raise AppError(message=f'Unknown report handler {fmt}')

    handler()
