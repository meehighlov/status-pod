import itertools

from status_pod.instagram.app.report import save_report
from status_pod.instagram.profile.common.actions import open_profile, get_users_info, close_context_window
from status_pod.instagram.profile.common.login import login, close_popups_after_login


def get_previous_followers_names():
    # TODO супер наивная хуйня, надо переделать
    try:
        with open('report.txt') as f:
            lines = f.readlines()

            start_line_index = lines.index('follow me')
            lines = lines[start_line_index:]
            lines = itertools.takewhile(lambda line: '-' not in line, lines)

            r = set(lines)
            print(r)
            return r
    except (FileNotFoundError, ValueError):
        return set()



def report_subscribtions_info(browser, result_path: str):  # noqa
    with browser:
        login(browser)
        close_popups_after_login(browser)
        open_profile(browser)
        f_i = get_users_info(browser, who='follows_me')
        close_context_window(browser)
        s_i = get_users_info(browser, who='i_am_follow')
        close_context_window(browser)

        f = f_i.nicknames
        s = s_i.nicknames

        mutual = f & s
        i_am_not_follow = f - s
        not_follow_me_back = s - f

        previous_f = get_previous_followers_names()

        report = {
            'total': [
                f'followers: {f_i.users_amount}',
                f'subscriptions: {s_i.users_amount}',
                f'mutual subscriptions: {len(mutual)}',
                f'i am not follow: {len(i_am_not_follow)}',
                f'not follow me back: {len(not_follow_me_back)}'
            ],
            'mutual': mutual,
            'i am not follow': i_am_not_follow,
            'follow me': f,
            'not follow me back': not_follow_me_back,
            'difference from previous followers list': previous_f.symmetric_difference(f) if previous_f else set()
        }

    save_report(path=result_path, report=report, fmt='txt')
