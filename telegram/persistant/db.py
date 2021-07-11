import sqlite3
from collections import namedtuple
from functools import wraps

from telegram.core import config


#TODO make things better with that
#TODO i don't like how it works now


def db_connection(f):
    @wraps(f)
    def db_connection_user(*args, **kwargs):
        connection = sqlite3.connect(config.DB_NAME)
        db = namedtuple('DB', 'connection cursor')
        kwargs['db'] = db(connection=connection, cursor=connection.cursor())
        try:
            result = f(*args, **kwargs)
        except Exception as e:
            # if any error occurred we need to close connection
            connection.close()
            print(f'something bad happened: {e}')
            return
        connection.commit()
        connection.close()
        return result
    return db_connection_user


@db_connection
def init_db(db):
    db.cursor.execute(
        '''
            create table if not exists payments (item text, price real, date text);
        '''
    )
