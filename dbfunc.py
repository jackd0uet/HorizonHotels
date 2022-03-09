import mysql.connector
from mysql.connector import errorcode

#MYSQL CONFIG VAR
hostname = "localhost"
username = "root"
password = "password"
db = "HH_DB"

def getConnection():
    try:
        conn = mysql.connector.connect(host=hostname,
                                    user=username,
                                    password=password,
                                    database=db)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('User name or password is incorrect.')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database cannot be found.')
        else:
            print(err)

    else:
        return conn