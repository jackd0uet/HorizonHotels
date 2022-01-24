import mysql.connector, dbfunc
conn = dbfunc.getConnection()   #connection to DB
DB_NAME = 'HORIZON_HOTELS'             #DB Name
TABLE_NAME = 'RESERVATION'

TABLE_DESCRIPTION = 'CREATE TABLE ' + TABLE_NAME + ' ( \
    reservationId VARCHAR(20)  NOT NULL, \
    customerId VARCHAR(20) NOT NULL, \
    hotelCity VARCHAR(20) NOT NULL, \
    roomId VARCHAR(20) NOT NULL, \
    dateBooked DATE NOT NULL, \
    startDate DATE NOT NULL, \
    endDate DATE NOT NULL, \
    PRIMARY KEY (reservationId), \
    FOREIGN KEY (customerId) REFERENCES CUSTOMER(customerId), \
    FOREIGN KEY (hotelCity) REFERENCES HOTEL(hotelCity), \
    FOREIGN KEY (roomId) REFERENCES ROOM(roomId));'

if conn != None:    #Checking if connection is None
    if conn.is_connected(): #Checking if connection is established
        print('MySQL Connection is established')                          
        dbcursor = conn.cursor()    #Creating cursor object
        dbcursor.execute('USE {};'.format(DB_NAME)) #use database        
        dbcursor.execute(TABLE_DESCRIPTION) 
        print('Table {} created successfully.'.format(TABLE_NAME))               
        conn.close() #Connection must be closed
    else:
        print('DB connection error')
else:
    print('DBFunc error')
