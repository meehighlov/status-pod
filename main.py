import sys

from status_pod.instagram.main import subs
from status_pod.instagram.analyze_posts.main import analyze_posts


if __name__ == '__main__':
    filename, script_name, *args = sys.argv

    script_name_to_script = {
        'subs': subs,
        'posts': analyze_posts
    }

    script = script_name_to_script[script_name]

    script(*args)
