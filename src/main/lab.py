import os
import sqlite3

"""
SQL sublanguage: DML (Data Manipulation Language)

To update a record we utilize the UPDATE keyword. The syntax for updating a record is as follows:
UPDATE table_name SET col_1 = val_1, col_2 = val_2, ...col_N = val_N WHERE condition;

NOTE: The WHERE condition is important because if you leave this out, that column will be updated throughout all
the records in the table.
"""

_LAB_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _read_sql(filename):
    with open(os.path.join(_LAB_DIR, filename), "r", encoding="utf-8") as f:
        return f.read().strip()


def problem1():
    """
    site_user table:
    |   id  |     firstname        |        lastname        |
    ----------------------------------------------------------
    |1      |'Steve'               |'Garcia'                |
    |2      |'Alexa'               |'Smith'                 |
    |3      |'Steve'               |'Jones'                 |
    |4      |'Brandon'             |'Smith'                 |
    |5      |'Adam'                |'Jones'                 |

    Problem 1: Update Alexa's last name to be 'Rush' in the site_user table.

    Sets up the site_user table, runs the student's statement against it, and returns the open connection so
    the caller can verify the update.
    """
    sql = _read_sql("problem1.sql")

    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE site_user (id INTEGER PRIMARY KEY AUTOINCREMENT, firstname varchar(100), lastname varchar(100));"
    )
    cur.execute("INSERT INTO site_user (firstname, lastname) VALUES ('Steve', 'Garcia');")
    cur.execute("INSERT INTO site_user (firstname, lastname) VALUES ('Alexa', 'Smith');")
    cur.execute("INSERT INTO site_user (firstname, lastname) VALUES ('Steve', 'Jones');")
    cur.execute("INSERT INTO site_user (firstname, lastname) VALUES ('Brandon', 'Smith');")
    cur.execute("INSERT INTO site_user (firstname, lastname) VALUES ('Adam', 'Jones');")
    conn.commit()

    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print(f"problem1: {e}\n")

    return conn
