import sqlite3

conn = sqlite3.connect('rasa.db')
c = conn.cursor()

for row in c.execute("pragma table_info(events)"):
    print(row)

print('------------------------------------------------')

for row in c.execute("SELECT * FROM events order by id desc limit 10 "):
    print(row)