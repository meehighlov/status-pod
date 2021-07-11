from app.report import save_report
from profile.common.actions import open_profile, get_users_info, close_window_with_users_list
from profile.common.login import login, close_popups_after_login


def subscribtions_info(browser, result_path: str):  # noqa
    with browser:
        login(browser)
        close_popups_after_login(browser)
        open_profile(browser)
        f_i = get_users_info(browser, who='follows_me')
        close_window_with_users_list(browser)
        s_i = get_users_info(browser, who='i_am_follow')
        close_window_with_users_list(browser)

        f = f_i.nicknames
        s = s_i.nicknames

        mutual = f & s
        i_am_not_follow = f - s
        not_follow_me_back = s - f

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
            'not follow me back': not_follow_me_back
        }

    save_report(path=result_path, report=report, fmt='txt')
