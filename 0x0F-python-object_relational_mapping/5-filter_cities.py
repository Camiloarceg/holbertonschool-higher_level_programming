#!/usr/bin/python3
""" script that takes in the name of a state as an argument
    and lists all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    mydb = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           password=sys.argv[2], database=sys.argv[3])
    mycursor = mydb.cursor()
    q = "SELECT cities.name\
        FROM cities, states\
        WHERE BINARY states.name = %s\
        AND cities.state_id = states.id\
        ORDER BY cities.id ASC"
    state = (sys.argv[4],)
    mycursor.execute(q, state)
    myresult = mycursor.fetchall()
    print(", ".join(row[0] for row in myresult))
    mycursor.close()
    mydb.close()
