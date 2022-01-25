import sys

from status_pod.instagram.main import subs
from status_pod.instagram.analyze_posts.main import analyze_posts
from status_pod.tg.core import init_bot


if __name__ == '__main__':
    filename, script_name, *args = sys.argv

    script_name_to_script = {
        'subs': subs,
        'posts': analyze_posts,
        'bot': init_bot
    }

    script = script_name_to_script[script_name]

    script(*args)
