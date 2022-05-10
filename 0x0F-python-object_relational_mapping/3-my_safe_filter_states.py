#!/usr/bin/python3
import sys
import MySQLdb
""" script that takes in arguments and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
    But this time, write one that is safe from MySQL injections!
"""
if __name__ == "__main__":
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    mycursor = mydb.cursor()
    q = "SELECT * FROM states\
        WHERE name LIKE BINARY %s ORDER BY id ASC"
    state = (sys.argv[4], )
    mycursor.execute(q, state)
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)
    mycursor.close()
    mydb.close()
