import sqlite3


def db_connection():
    '''
    :return: DB cursor
    '''
    conn = sqlite3.connect('rasa.db')
    c = conn.cursor()

    return c


def db_query(conn):
    '''db_query
    Prints rasa.db structure and last 10 tuples
    '''
    for row in conn.execute("pragma table_info(events)"):
        print(row)

    print('------------------------------------------------')

    for row in conn.execute("SELECT * FROM events order by id desc limit 10 "):
        print(row)


if __name__ == "__main__":
    conn = db_connection()
    db_query(conn)