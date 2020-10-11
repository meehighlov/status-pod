import sqlite3

from collections import namedtuple

from core.config import config


def create_tables(cursor):
    cursor.execute(
        '''
            create table if not exists payments (item text, price real, date text);
        '''
    )
    cursor.execute(
        '''
            create table if not exists payments (item text, price real, date text);
        '''
    )


def init_db(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    create_tables(cursor)
    connection.commit()
    db = namedtuple('DB', 'connection cursor')
    connection.close()
    print('db initialized')
    return db(connection=connection, cursor=cursor)


db = init_db(config.DB_NAME)
