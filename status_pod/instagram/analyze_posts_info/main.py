from datetime import datetime, timedelta


def get_posts_for_current_context():
    return []


def get_post_date(post):
    return ''


def open_feed():
    pass


def get_post_owner_name(post):
    return ''


def first_comment_is_written_by_post_owner(post):
    return True


def get_first_comment(post):
    return ''


def has_comment_triggers(comment: str):
    return True


def notify():
    pass


def scroll_down_feed():
    pass


def create_post_hash(post):
    post_owner = get_post_owner_name(post)
    post_date = get_post_date(post)

    return hash(post_owner + post_date)


def analyze_posts(browser):
    open_feed(browser)

    post_date = datetime.utcnow()  # temporary
    edge_date = post_date + timedelta(days=1)  # temporary
    viewed_posts = set()

    while post_date < edge_date:
        posts = get_posts_for_current_context(browser)
        for post in posts:

            post_hash = create_post_hash(post)
            if post_hash in viewed_posts:
                continue

            viewed_posts.add(post_hash)

            if not first_comment_is_written_by_post_owner(post):
                continue

            comment = get_first_comment(post)

            if has_comment_triggers(comment):
                notify()
            
            post_date = get_post_date(post)

        scroll_down_feed(browser)
