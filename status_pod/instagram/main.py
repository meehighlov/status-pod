import signal

from status_pod.instagram.app.browser import chrome
from status_pod.app.config import config
from status_pod.instagram.app.exceptions import TimeoutAppError
from status_pod.instagram.profile.subscriptions import subscribtions_info


def timeout_handler(signum, frame):
    raise TimeoutAppError()


def launch(*args, **kwargs):
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(config.TIMEOUT_FOR_INSTA_TASK_EXECUTION_SEC)
    subscribtions_info(chrome, result_path=config.REPORT_PATH)
    signal.alarm(0)


if __name__ == '__main__':
    launch()
