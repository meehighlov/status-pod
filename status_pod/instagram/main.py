import signal

from status_pod.instagram.app.browser import create_browser_instance
from status_pod.app.config import config
from status_pod.app.exceptions import TimeoutAppError
from status_pod.instagram.profile.subscriptions import report_subscribtions_info


def timeout_handler(signum, frame):
    raise TimeoutAppError()


def subs(*args, **kwargs):
    # signal.signal(signal.SIGALRM, timeout_handler)
    # signal.alarm(config.TIMEOUT_FOR_INSTA_TASK_EXECUTION_SEC)
    browser = create_browser_instance()
    results = report_subscribtions_info(browser, result_path=config.REPORT_PATH)
    # signal.alarm(0)

    return results


if __name__ == '__main__':
    subs()
