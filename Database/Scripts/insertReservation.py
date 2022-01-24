import mysql.connector, dbfunc
conn = dbfunc.getConnection()   #connection to DB
DB_NAME = 'HORIZON_HOTELS'             #DB Name
TABLE_NAME = 'RESERVATION'
resId = input('Enter reservationId: ')
custId = input('Enter Customer ID: ')
hotelCity = input('Enter the city the hotel is in: ')
roomId = input("Enter room id: ")
booked = input("Enter date booked: ")
start = input("Enter start date: ")
end = input("Enter end date: ")
# here you should perform data validation 
# syntax as well as semantics 

INSERT_statement = 'INSERT INTO ' + TABLE_NAME + ' (\
    reservationId, customerId, hotelCity, roomId, dateBooked, startDate, endDate) VALUES (%s, %s, %s, %s, %s, %s, %s);'    

if conn != None:    #Checking if connection is None
    if conn.is_connected(): #Checking if connection is established
        print('MySQL Connection is established')                          
        dbcursor = conn.cursor()    #Creating cursor object
        dbcursor.execute('USE {};'.format(DB_NAME)) #use database        
        dataset = (resId, custId, hotelCity, roomId, booked, start, end)        
        dbcursor.execute(INSERT_statement, dataset)   
        conn.commit()              
        print('INSERT query executed successfully.') 
        dbcursor.close()              
        conn.close() #Connection must be closed
    else:
        print('DB connection error')
else:
    print('DBFunc error')
