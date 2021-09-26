from pprint import pprint
import sqlite3

def fetch_alerts():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    rows = cursor.execute("Select * from alerts Group By name").fetchall()
    # cursor.close()
    return rows

def create_test_alerts():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    test_alerts = [
        ("NAME1", "CLASS", "EMAIL", "MONTH-DAY-YEAR TIME", "PHONE NUMBER"),
        ("NAME2", "CLASS", "EMAIL", "MONTH-DAY-YEAR TIME", "PHONE NUMBER"),
        ("NAME3", "CLASS", "EMAIL", "MONTH-DAY-YEAR TIME", "PHONE NUMBER"),
        ("NAME4", "CLASS", "EMAIL", "MONTH-DAY-YEAR TIME", "PHONE NUMBER")
    ]
    statement = "insert into alerts (name, class, email, due_date, phone_number) values (?, ?, ?, ?, ?)"
    cursor.executemany(statement,test_alerts)
    connection.commit()
    cursor.close()

def create_alerts_table(drop=False):
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    if drop:
        cursor.execute('DROP TABLE alerts')
    cursor.execute('''CREATE TABLE alerts
    (id integer primary key autoincrement, name text, class text, email text, due_date datetime, phone_number integer)''')
    cursor.close()

# You *must* comment these function calls out once you have called them once 
# Otherwise you will be using the same data but requesting additional database commits that you don't need

# create_alerts_table(drop=True)
# create_test_alerts()
# pprint(fetch_alerts())