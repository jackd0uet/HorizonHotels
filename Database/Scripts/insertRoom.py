import mysql.connector, dbfunc
conn = dbfunc.getConnection()   #connection to DB
DB_NAME = 'HORIZON_HOTELS'             #DB Name
TABLE_NAME = 'ROOM'
id = input('Enter roomId: ')
desc = input('Enter Room Descrpition: ')
type = input('Enter Type: ')
# here you should perform data validation 
# syntax as well as semantics 

INSERT_statement = 'INSERT INTO ' + TABLE_NAME + ' (\
    roomId, roomDescription, roomType) VALUES (%s, %s, %s);'    

if conn != None:    #Checking if connection is None
    if conn.is_connected(): #Checking if connection is established
        print('MySQL Connection is established')                          
        dbcursor = conn.cursor()    #Creating cursor object
        dbcursor.execute('USE {};'.format(DB_NAME)) #use database        
        dataset = (id, desc, type)        
        dbcursor.execute(INSERT_statement, dataset)   
        conn.commit()              
        print('INSERT query executed successfully.') 
        dbcursor.close()              
        conn.close() #Connection must be closed
    else:
        print('DB connection error')
else:
    print('DBFunc error')
