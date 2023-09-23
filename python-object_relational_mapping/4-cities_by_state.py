"""importing MySQLdb"""

import MySQLdb as Mydb
import sys


def cities():
    """def states"""

    db_connect = Mydb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM cities")
    rows_selected = db_cursor.fetchall()
    for row in rows_selected:
        print(row)
if __name__ == "__main__":
    cities()
