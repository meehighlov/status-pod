import signal

from status_pod.instagram.app.browser import chrome
from status_pod.app import config
from status_pod.instagram.app.exceptions import TimeoutAppError
from status_pod.instagram.profile.subscriptions import subscribtions_info


def timeout_handler(signum, frame):
    raise TimeoutAppError()


def launch(*args, **kwargs):
    subscribtions_info(chrome, result_path=config.REPORT_PATH)


if __name__ == '__main__':
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(config.TIMEOUT_FOR_INSTA_TASK_EXECUTION_SEC)
    launch()
    signal.alarm(0)
