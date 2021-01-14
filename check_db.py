import sqlite3


def db_connection():
    """
    	:return: DB cursor
    """
    conn = sqlite3.connect('rasa.db')
    cur = conn.cursor()

    print("Database connected")

    return cur


def db_query(cur, query):
    """db_query
    Prints rasa.db structure and last 10 tuples
    """
    for row in cur.execute("pragma table_info(events)"):
        print(row)

    print('------------------------------------------------')

    for row in cur.execute(query):
        print(row)


if __name__ == "__main__":

    query = "SELECT * FROM events order by id desc limit 10 "

    try:
        cur = db_connection()
        db_query(cur, query)

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

    finally:
        if(cur):
            cur.close()
            print("Database connection closed")
