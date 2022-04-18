import mysql.connector, dbfunc
i=0
while i < 16:
    conn = dbfunc.getConnection()
    DB_NAME = 'HH_DB'
    TABLE_NAME = 'hotel'


    INSERT_STATEMENT = "INSERT INTO " + TABLE_NAME + "(roomType, hotelCity, address, fare, offPeakFare) VALUES ('Family', 'Swansea', 'SA1 1DE', 120, 50);"
 
    if conn != None:
        if conn.is_connected():
            print("CONNECTION ESTABLISHED")
            dbcursor = conn.cursor()
            dbcursor.execute("USE {};".format(DB_NAME))
            dbcursor.execute(INSERT_STATEMENT)
            conn.commit()
            print("EXECUTED")
            dbcursor.close()
            conn.close()
            i=i+1
        else:
            print("COnnection error")
    else:
        print("DB FUNC ERROR")