"""importing MySQLdb"""

import MySQLdb as Mydb
import sys

def states():
    """def states"""
    
    db_connect = Mydb.connect(host="localhost", port="3306", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states WHERE name LIKE %s", (sys.argv[4]))
    rows_selected = db_cursor.fetchall()
    for row in rows_selected:
        print(row)
if __name__ == "__main__":
    states()