# Horizon Hotels
# app.py V1
# Jack Douet

# Import required modules
from crypt import methods
from distutils.log import error
from pydoc import render_doc
from tabnanny import check
from flask import Flask, render_template, request, url_for, jsonify, redirect, session
from datetime import datetime, date
from functools import wraps
from matplotlib.style import available
from numpy import double
from passlib.hash import sha256_crypt
import dbfunc
import mysql.connector
import gc
import hashlib
from dateutil.relativedelta import relativedelta


# Setup flask app
app = Flask(__name__)

# Create secret key for password creation
app.config.update(SECRET_KEY='osd(7:?[??jr??M7?H?')


# Index route
@app.route('/')
def index():
    return render_template('index.html')

# City selection route


@app.route('/our_cities/')
def ourCities():
    # Connect to DB
    conn = dbfunc.getConnection()

    # Check connection
    if conn != None:
        print("CONNECTED TO DATABASE: HH_DB")
        dbcursor = conn.cursor()

        # Fetch all unique hotels and feed them into html template
        dbcursor.execute("SELECT DISTINCT hotelCity FROM hotel;")
        cities = dbcursor.fetchall()
        data = []
        for city in cities:
            data.append(city)

         # Set availability defaults to True for all hotels so that they all will display on our cities page before date is selected.
        availability = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        return render_template('Our_cities.html', cities=data, availability=availability, date=False)
    # Connection error handling.
    else:
        print("CANNOT CONNECT TO HH_DB")
        error = "conn"
        return render_template("error.html", error=error)


# Cities pre booking form
@app.route('/our_cities_form/', methods=['POST', 'GET'])
def ourCitiesForm():
    # Gather data from form if POST method
    if request.method == 'POST':
        start = request.form['sDate']
        end = request.form['eDate']
        guests = request.form['guests']

        # Connect to HH_DB
        conn = dbfunc.getConnection()
        if conn != None:
            print("CONNECTED TO DATABASE: HH_DB")
            dbcursor = conn.cursor()

            # Empty list for availability
            availability = []

            # Fetch all unique hotels and feed them into html template
            dbcursor.execute("SELECT DISTINCT hotelCity FROM hotel;")
            cities = dbcursor.fetchall()
            data = []
            for city in cities:
                data.append(city)

            # Check all hotels booked rooms for selected date range and compare to amount of rooms at hotel.
            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Aberdeen" AND maxOccupancy <= %s;', (guests, ))
            aberdeenTotalRooms = dbcursor.fetchall()
            aberdeenTotalRooms = aberdeenTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Aberdeen" AND guests <= %s;', (start, end, guests))
            aberdeenRoomsBooked = dbcursor.fetchall()
            aberdeenRoomsBooked = aberdeenRoomsBooked[0][0]

            # For each hotel give 1 value for available else 0 for unavailable and put into availability list.
            if aberdeenTotalRooms > aberdeenRoomsBooked:
                aberdeen = 1
            else:
                aberdeen = 0

            availability.append(aberdeen)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Belfast" AND maxOccupancy <= %s;', (guests, ))
            belfastTotalRooms = dbcursor.fetchall()
            belfastTotalRooms = belfastTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Belfast" AND guests <= %s;', (start, end, guests))
            belfastRoomsBooked = dbcursor.fetchall()
            belfastRoomsBooked = belfastRoomsBooked[0][0]

            if belfastTotalRooms > belfastRoomsBooked:
                belfast = 1
            else:
                belfast = 0

            availability.append(belfast)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Birmingham" AND maxOccupancy <= %s;', (guests, ))
            birminghamTotalRooms = dbcursor.fetchall()
            birminghamTotalRooms = birminghamTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Birmingham" AND guests <= %s;', (start, end, guests))
            birminghamRoomsBooked = dbcursor.fetchall()
            birminghamRoomsBooked = birminghamRoomsBooked[0][0]

            if birminghamTotalRooms > birminghamRoomsBooked:
                birmingham = 1
            else:
                birmingham = 0

            availability.append(birmingham)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Bristol" AND maxOccupancy <= %s;', (guests, ))
            bristolTotalRooms = dbcursor.fetchall()
            bristolTotalRooms = bristolTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Bristol" AND guests <= %s;', (start, end, guests))
            bristolRoomsBooked = dbcursor.fetchall()
            bristolRoomsBooked = bristolRoomsBooked[0][0]

            if bristolTotalRooms > bristolRoomsBooked:
                bristol = 1
            else:
                bristol = 0

            availability.append(bristol)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Cardiff" AND maxOccupancy <= %s;', (guests, ))
            cardiffTotalRooms = dbcursor.fetchall()
            cardiffTotalRooms = cardiffTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Cardiff" AND guests <= %s;', (start, end, guests))
            cardiffRoomsBooked = dbcursor.fetchall()
            cardiffRoomsBooked = cardiffRoomsBooked[0][0]

            if cardiffTotalRooms > cardiffRoomsBooked:
                cardiff = 1
            else:
                cardiff = 0

            availability.append(cardiff)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Edinburgh" AND maxOccupancy <= %s;', (guests, ))
            edinburghTotalRooms = dbcursor.fetchall()
            edinburghTotalRooms = edinburghTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Edinburgh" AND guests <= %s;', (start, end, guests))
            edinburghRoomsBooked = dbcursor.fetchall()
            edinburghRoomsBooked = edinburghRoomsBooked[0][0]

            if edinburghTotalRooms > edinburghRoomsBooked:
                edinburgh = 1
            else:
                edinburgh = 0

            availability.append(edinburgh)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Glasgow" AND maxOccupancy <= %s;', (guests, ))
            glasgowTotalRooms = dbcursor.fetchall()
            glasgowTotalRooms = glasgowTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Glasgow" AND guests <= %s;', (start, end, guests))
            glasgowRoomsBooked = dbcursor.fetchall()
            glasgowRoomsBooked = glasgowRoomsBooked[0][0]

            if glasgowTotalRooms > glasgowRoomsBooked:
                glasgow = 1
            else:
                glasgow = 0

            availability.append(glasgow)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "London" AND maxOccupancy <= %s;', (guests, ))
            londonTotalRooms = dbcursor.fetchall()
            londonTotalRooms = londonTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "London" AND guests <= %s;', (start, end, guests))
            londonRoomsBooked = dbcursor.fetchall()
            londonRoomsBooked = londonRoomsBooked[0][0]

            if londonTotalRooms > londonRoomsBooked:
                london = 1
            else:
                london = 0

            availability.append(london)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Manchester" AND maxOccupancy <= %s;', (guests, ))
            manchesterTotalRooms = dbcursor.fetchall()
            manchesterTotalRooms = manchesterTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Manchester" AND guests <= %s;', (start, end, guests))
            manchesterRoomsBooked = dbcursor.fetchall()
            manchesterRoomsBooked = manchesterRoomsBooked[0][0]

            if manchesterTotalRooms > manchesterRoomsBooked:
                manchester = 1
            else:
                manchester = 0

            availability.append(manchester)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Newcastle" AND maxOccupancy <= %s;', (guests, ))
            newcastleTotalRooms = dbcursor.fetchall()
            newcastleTotalRooms = newcastleTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Newcastle" AND guests <= %s;', (start, end, guests))
            newcastleRoomsBooked = dbcursor.fetchall()
            newcastleRoomsBooked = newcastleRoomsBooked[0][0]

            if newcastleTotalRooms > newcastleRoomsBooked:
                newcastle = 1
            else:
                newcastle = 0

            availability.append(newcastle)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Norwich" AND maxOccupancy <= %s;', (guests, ))
            norwichTotalRooms = dbcursor.fetchall()
            norwichTotalRooms = norwichTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Norwich" AND guests <= %s;', (start, end, guests))
            norwichRoomsBooked = dbcursor.fetchall()
            norwichRoomsBooked = norwichRoomsBooked[0][0]

            if norwichTotalRooms > norwichRoomsBooked:
                norwich = 1
            else:
                norwich = 0

            availability.append(norwich)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Nottingham" AND maxOccupancy <= %s;', (guests, ))
            nottinghamTotalRooms = dbcursor.fetchall()
            nottinghamTotalRooms = nottinghamTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Nottingham" AND guests <= %s;', (start, end, guests))
            nottinghamRoomsBooked = dbcursor.fetchall()
            nottinghamRoomsBooked = nottinghamRoomsBooked[0][0]

            if nottinghamTotalRooms > nottinghamRoomsBooked:
                nottingham = 1
            else:
                nottingham = 0

            availability.append(nottingham)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Oxford" AND maxOccupancy <= %s;', (guests, ))
            oxfordTotalRooms = dbcursor.fetchall()
            oxfordTotalRooms = oxfordTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Oxford" AND guests <= %s;', (start, end, guests))
            oxfordRoomsBooked = dbcursor.fetchall()
            oxfordRoomsBooked = oxfordRoomsBooked[0][0]

            if oxfordTotalRooms > oxfordRoomsBooked:
                oxford = 1
            else:
                oxford = 0

            availability.append(oxford)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Plymouth" AND maxOccupancy <= %s;', (guests, ))
            plymouthTotalRooms = dbcursor.fetchall()
            plymouthTotalRooms = plymouthTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Plymouth" AND guests <= %s;', (start, end, guests))
            plymouthRoomsBooked = dbcursor.fetchall()
            plymouthRoomsBooked = plymouthRoomsBooked[0][0]

            if plymouthTotalRooms > plymouthRoomsBooked:
                plymouth = 1
            else:
                plymouth = 0

            availability.append(plymouth)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Swansea" AND maxOccupancy <= %s;', (guests, ))
            swanseaTotalRooms = dbcursor.fetchall()
            swanseaTotalRooms = swanseaTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Swansea" AND guests <= %s;', (start, end, guests))
            swanseaRoomsBooked = dbcursor.fetchall()
            swanseaRoomsBooked = swanseaRoomsBooked[0][0]

            if swanseaTotalRooms > swanseaRoomsBooked:
                swansea = 1
            else:
                swansea = 0

            availability.append(swansea)

            # Close connections.
            dbcursor.close()
            conn.close()
            print("DISCONNECTED FROM HH_DB!")

            return render_template('Our_cities.html', cities=data, availability=availability, date=True, startDate=start, endDate=end, guests=guests)

        # Connection error handling.
        else:
            print("CANNOT CONNECT TO HH_DB")
            error = "conn"
            return render_template("error.html", error=error)


# Login route
@app.route('/account/login/')
def log_in():
    return render_template('Account/Log_in.html')

# My account route


@app.route('/account/my_account/')
def myAccount():
    # Connection to DB
    conn = dbfunc.getConnection()

    if conn != None:
        print("CONNECTED TO DATABASE: HH_DB")
        dbcursor = conn.cursor()

        # Count user bookings
        dbcursor.execute(
            'SELECT COUNT(*) FROM bookings WHERE customerId = %s;', (session.get('userId'), )
        )
        bookedCount = dbcursor.fetchone()[0]

        # Select all bookings for customer whose ID is provided using session variable.
        dbcursor.execute(
            'SELECT * FROM FULLBOOKINGINFO WHERE customerId = %s;', (session.get('userId'), ))

        rows = dbcursor.fetchall()
        datarows = []

        for row in rows:
            data = list(row)
            datarows.append(data)

        # Select all cancelled bookings for customer whose ID is provided using session variable.
        dbcursor.execute(
            "SELECT * FROM cancelledBookings WHERE customerId = %s", (session.get('userId'), ))
        rowsTwo = dbcursor.fetchall()
        dataRowsTwo = []

        for row in rowsTwo:
            dataTwo = list(row)
            dataRowsTwo.append(dataTwo)

        # Count the amount of cancelled bookings.
        dbcursor.execute(
            "SELECT COUNT(*) FROM cancelledBookings WHERE customerId = %s", (session.get('userId'), ))
        cancelledCount = dbcursor.fetchone()[0]

        # Close connection.
        dbcursor.close()
        conn.close()
        print("DISCONNECTED FROM HH_DB!")

        # If the user has been routed to myAccount through the booking process return user to booking pages.
        if 'city' in session:
            return (redirect(url_for('booking')))
        # Otherwise show the user their account.
        else:
            return render_template('Account/My_account.html', bookedCount=bookedCount, bookingData=datarows, cancelledData=dataRowsTwo, cancelledCount=cancelledCount)
    # Connection error handling.
    else:
        print("CANNOT CONNECT TO HH_DB")
        error = "conn"
        return render_template("error.html", error=error)

# Modify booking route
@app.route('/account/modify_booking/', methods=['POST', 'GET'])
def modify():
    # Check form has been submitted.
    if request.method == 'POST':
        # Collect bookingID from form.
        bookingId = request.form['modifyBooking']

        # Connect to DB.
        conn = dbfunc.getConnection()

        # Check connection.
        if conn != None:
            print("CONNECTED TO DATABASE: HH_DB")
            dbcursor = conn.cursor()
            # Use booking ID to bring up the whole booking info.
            dbcursor.execute(
                "SELECT * FROM bookings WHERE bookingId = %s;", (bookingId, ))
            rows = dbcursor.fetchall()
            datarows = []

            for row in rows:
                data = list(row)
                datarows.append(data)
            dbcursor.close()
            conn.close()
            print("DISCONNECTED FROM HH_DB!")

            # Calculate the difference between todays date and booking date for use in refund logic.
            todayDate = date.today()
            dateDifference = datarows[0][4] - todayDate
            dateDifference = dateDifference.days

            return render_template('Account/modifyBooking.html', bookingInfo=datarows[0], daysLeft=dateDifference)

        # Connection error handling.
        else:
            print("CANNOT CONNECT TO HH_DB")
            error = "conn"
            return render_template("error.html", error=error)

# Cancel booking route
@app.route('/account/cancel_booking/', methods=['POST', 'GET'])
def cancel():
    # Validate POST request
    if request.method == 'POST':
        # Gather variables from form
        daysBeforeBooking = int(request.form['Cancel'])
        bookingId = request.form['bookingId']
        customerId = request.form['customerId']
        roomId = request.form['roomId']
        dateBooked = request.form['dateBooked']
        startDate = request.form['startDate']
        endDate = request.form['endDate']
        guests = request.form['guests']
        totalPaid = float(request.form['totalPaid'])
        currency = request.form['currency']

        # Business logic for refund amount.
        if daysBeforeBooking > 60:
            totalRefund = totalPaid
        elif daysBeforeBooking <= 60 and daysBeforeBooking > 30:
            totalRefund = totalPaid / 2
        else:
            totalRefund = 0

        todaysDate = date.today()

        # Connect to DB
        conn = dbfunc.getConnection()
        if conn != None:
            print("CONNECTED TO DATABASE: HH_DB")
            dbcursor = conn.cursor()

            # Create new record in cancelledBookings table and delete booking from bookings table.
            dbcursor.execute("INSERT INTO cancelledBookings (bookingId, customerId, roomId, dateBooked, \
            startDate, endDate, dateCancelled, guests, totalFare, totalRefunded, currency) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (bookingId, customerId, roomId, dateBooked,
                                                                startDate, endDate, todaysDate, guests, totalPaid, totalRefund, currency,))
            dbcursor.execute(
                "DELETE FROM bookings WHERE bookingId = %s;", (bookingId, ))
            conn.commit()
            print("Booking " + bookingId + " cancelled!")
            dbcursor.close()
            conn.close()
            print("DISCONNECTED FROM HH_DB!")

            return render_template('/Account/confirm_cancel.html', bookId=bookingId, refund=totalRefund, currency=currency)
        # Connection error handling.
        else:
            print("CANNOT CONNECT TO HH_DB")
            error = "conn"
            return render_template("error.html", error=error)

# No account route
@app.route('/account/no_account/')
def noAccount():
    return render_template('Account/no_account.html')

# Account route
@app.route('/account/')
def account():
    # If user is admin redirect to admin hub else to regular user page
    if session.get('logged_in') == True:
        if session.get('userType') == "ADMIN":
            return redirect(url_for('adminHub'))
        else:
            return redirect(url_for('myAccount'))
    # If not logged in redirect to no account route.
    else:
        return redirect(url_for('noAccount'))

# Admin hub route
@app.route('/account/adminHub/')
def adminHub():
    # Connect to DB
    conn = dbfunc.getConnection()

    if conn != None:
        print("CONNECTED TO DATABASE: HH_DB")
        dbcursor = conn.cursor()
        # Select all unique hotels.
        dbcursor.execute("SELECT DISTINCT hotelCity FROM hotel;")
        cities = dbcursor.fetchall()
        data = []
        for city in cities:
            data.append(city)

        return render_template('Account/admin.html', citiesData=data,)

    # Connection error handling.
    else:
        print("CANNOT CONNECT TO HH_DB")
        error = "conn"
        return render_template("error.html", error=error)

#Comments route
@app.route('/account/comments/')
def adminComments():
    # Connect to DB
    conn = dbfunc.getConnection()

    if conn != None:
        print("CONNECTED TO DATABASE: HH_DB")
        dbcursor = conn.cursor()
        # Retrieve comments
        dbcursor.execute("SELECT * FROM comments;")
        rows = dbcursor.fetchall()
        datarows = []
        for row in rows:
            data = list(row)
            datarows.append(data)

        return render_template('Account/display_comments.html', commentsData=datarows)
    # Connection error handling.
    else:
        print("CANNOT CONNECT TO HH_DB")
        error = "conn"
        return render_template("error.html", error=error)

# Check bookings route for admin user
@app.route('/check-bookings/', methods=['POST', 'GET'])
def check_bookings():
    # Check POST request
    if request.method == 'POST':
        # Pull variables from form
        startDate = request.form['startDate']
        endDate = request.form['endDate']
        city = request.form['hotel']

        # Connect to DB
        conn = dbfunc.getConnection()

        # Check DB connection
        if conn != None:
            print("CONNECTED TO DATABASE: HH_DB")
            dbcursor = conn.cursor()

            # Select all bookings within time frame provided
            dbcursor.execute(
                "SELECT * FROM fullbookinginfo WHERE hotelCity = %s AND startDate BETWEEN %s AND %s;", (city, startDate, endDate))
            rows = dbcursor.fetchall()
            datarows = []
            for row in rows:
                data = list(row)
                datarows.append(data)

            return render_template('Account/check_bookings.html', bookingData=datarows)
        # Connection error handling.
        else:
            print("CANNOT CONNECT TO HH_DB")
            error = "conn"
            return render_template("error.html", error=error)


# Sign up route
@app.route('/account/signup/')
def signup():
    return render_template('Account/Sign_up.html')

# Sign up form route


@app.route('/sign-up/', methods=['POST', 'GET'])
def sign_up():
    # Check POST request
    if request.method == 'POST':
        # Create variables from form
        firstName = request.form['fname']
        lastName = request.form['lname']
        dateOfBirth = request.form['dob']
        postcode = request.form['postcode']
        email = request.form['email']
        password = request.form['password']
        passwordConfirm = request.form['confpassword']

        # Check for password equality
        if password == passwordConfirm:
            # Connect to DB
            conn = dbfunc.getConnection()
            # Check DB connection
            if conn != None:
                print("CONNECTED TO DATABASE: HH_DB")
                dbcursor = conn.cursor()

                # Create hashed password
                hashedPassword = sha256_crypt.hash((str(password)))
                # Check user does not already exist
                verifyQuery = "SELECT * FROM customer WHERE email = %s;"
                dbcursor.execute(verifyQuery, (email,))
                rows = dbcursor.fetchall()

                if dbcursor.rowcount > 0:
                    print("USER ALREADY EXISTS")
                    error = "email"
                    return render_template("error.html", error=error)
                # Otherwise create user.
                else:
                    dbcursor.execute('INSERT INTO customer(fName, lName, dob, postcode, \
                    email, password) VALUES (%s, %s, %s, %s, %s, %s);', (firstName,
                                                                         lastName, dateOfBirth, postcode, email, hashedPassword))
                    conn.commit()
                    print("USER CREATED SUCCESSFULLY")
                    dbcursor.close()
                    conn.close()
                    print("DISCONNECTED FROM HH_DB!")

                    return redirect(url_for('log_in'))

            # Connection error handling
            else:
                print("CANNOT CONNECT TO HH_DB")
                error = "conn"
                return render_template("error.html", error=error)

        else:
            return redirect(url_for('signup'))

# Login route
@app.route('/login/', methods=['POST', 'GET'])
def login():
    form = {}

    # Check request method
    if request.method == "POST":
        # Grab variables from form
        email = request.form['email']
        password = request.form['password']
        form = request.form

        # Check email and password have been entered correctly
        if email != None and password != None:
            conn = dbfunc.getConnection()
            if conn != None:
                print("CONNECTED TO HH_DB!")
                dbcursor = conn.cursor()
                dbcursor.execute("SELECT password FROM customer WHERE email = %s;",
                                 (email,))
                data = dbcursor.fetchone()

                # Error handling for incorrect email combo.
                if dbcursor.rowcount < 1:
                    error = "login"
                    dbcursor.close()
                    print("USER ENTERED INCORRECT DETAILS")
                    return render_template("error.html", error=error)

                else:
                    # Check password
                    if sha256_crypt.verify(request.form['password'], str(data[0])):
                        conn = dbfunc.getConnection()
                        # If correct connect to DB.
                        if conn != None:
                            print("CONNECTED TO HH_DB!")
                            dbcursor = conn.cursor()
                            # Get user details
                            dbcursor.execute(
                                "SELECT fName, lName, customerId, userType FROM customer WHERE email = %s;", (email, ))
                            data = dbcursor.fetchall()
                            data = data[0]
                            # Close connection to DB
                            dbcursor.close()
                            conn.close()
                            print("DISCONNECTED FROM HH_DB!")

                            # Create session variables
                            session['logged_in'] = True
                            session['email'] = request.form['email']
                            session['name'] = data[0] + " " + data[1]
                            session['userId'] = data[2]
                            session['userType'] = data[3]

                            # Redirect user to account page
                            print('USER ' + str(session['userId']) + ' LOGGED IN')
                            return redirect(url_for('account'))

                        # Connection error handling
                        else:
                            print("CANNOT CONNECT TO HH_DB")
                            error = "conn"
                            return render_template("error.html", error=error)
                    # Incorrect details
                    else:
                        error = "login"
                        print("USER ENTERED INCORRECT DETAILS")
                        return render_template("error.html", error=error)

            # Connection error handling
            else:
                print("CANNOT CONNECT TO HH_DB")
                error = "conn"
                return render_template("error.html", error=error)
        # No details entered
        else:
            print("NO DETAILS ENTERED")
            error = "login"
            return render_template("error.html", error=error)

# logout route


@app.route('/account/my_account/logout/')
def logout():
    # Get rid of all session variables and set logout to true.
    session.clear()
    logout = True
    return render_template('index.html', logout=logout)

# Booking route


@app.route('/book/', methods=['POST', 'GET'])
def booking():
    # Check request method
    if request.method == 'POST':
        # Create session variables from form in case user is not logged in.
        session['room'] = request.form['roomType']
        session['start'] = request.form['start-date']
        session['end'] = request.form['end-date']
        session['noOfGuests'] = request.form['guest-no']
        session['city'] = request.form['city']

    # Extract session variables into local variables
    room = session['room']
    start = session['start']
    end = session['end']
    noOfGuests = session['noOfGuests']
    city = session['city']

    # Create proper start and end date variables in correct format.
    startDate = datetime.strptime(start, '%Y-%m-%d')
    endDate = datetime.strptime(
        end, '%Y-%m-%d')
    totalNights = endDate - startDate

    # Create lookup list
    lookup = [city, start, end, noOfGuests, totalNights.days, room]

    # Check session to see if user is logged in
    if session.get('logged_in') == True:

        # Connect to DB
        conn = dbfunc.getConnection()
        # Check DB connection
        if conn != None:
            print("CONNECTED TO DATABASE: HH_DB")
            dbcursor = conn.cursor()

            # Look up count of all rooms with room type and hotel that user has selected.
            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = %s and roomType = %s;', (city, room))
            totalRooms = dbcursor.fetchall()
            totalRooms = totalRooms[0][0]

            # Look up count of booked rooms with type, hotel, start and end date that user has selected.
            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and roomType = %s and hotelCity = %s;', (start, end, room, city))
            roomsBooked = dbcursor.fetchall()
            roomsBooked = roomsBooked[0][0]

            # Select unbooked rooms from users selection.
            dbcursor.execute('SELECT * FROM hotel WHERE NOT EXISTS (SELECT * FROM bookings WHERE bookings.roomId = hotel.roomId and bookings.startDate = %s and bookings.endDate = %s) and hotelCity = %s and roomType = %s;', (start, end, city, room))
            rows = dbcursor.fetchall()
            datarows = []

            # Select Standard room data from user selected hotel for business logic.
            dbcursor.execute(
                'SELECT fare, offPeakFare FROM hotel WHERE roomType = "Standard" and hotelCity = %s', (city, ))
            standardRoomData = dbcursor.fetchall()
            standardRoomData = standardRoomData[0]

            # Calculate peak times
            peakStart = datetime(startDate.year, 4, 1)
            peakEnd = datetime(startDate.year, 10, 1)

            # calculate booking discount
            todaysDate = datetime.today()
            dateDifference = startDate - todaysDate
            dateDifference = dateDifference.days

            if dateDifference > 80:
                discount = .8
            elif dateDifference >= 60 and dateDifference <= 79:
                discount = .9
            elif dateDifference >= 45 and dateDifference <= 59:
                discount = .95
            else:
                discount = 1

            # Check if there is availability in selected hotel.
            if roomsBooked < totalRooms:
                # Calculate price for user based on their selections
                for row in rows:
                    data = list(row)
                    if peakStart <= startDate <= peakEnd and peakStart <= endDate <= peakEnd:
                        if room == "Double" and int(noOfGuests) > 1:
                            doubleIncrease = standardRoomData[0] * .1
                        else:
                            doubleIncrease = 0
                        fare = doubleIncrease
                        fare = fare + \
                            ((int(row[4]) * int(totalNights.days)))
                        fare = fare * discount
                        peakStatus = True
                    else:
                        if room == "Double" and int(noOfGuests) > 1:
                            doubleIncrease = standardRoomData[1] * 0.1
                        else:
                            doubleIncrease = 0
                        fare = doubleIncrease
                        fare = doubleIncrease + \
                            ((int(row[5]) * int(totalNights.days)))
                        fare = fare * discount
                        peakStatus = False

                    # Work out fare in other currencies
                    fareEuros = fare * 1.2
                    fareUSD = fare * 1.6

                    # Append fares to booking data
                    data.append(fare)
                    data.append(fareEuros)
                    data.append(fareUSD)

                    datarows.append(data)

                # Close DB connection.
                dbcursor.close()
                conn.close()
                print("DISCONNECTED FROM HH_DB!")

                # Remove booking data from session.
                session.pop('room', None)
                session.pop('start', None)
                session.pop('noOfGuests', None)
                session.pop('city', None)

                return render_template('Booking/book.html', bookingSet=datarows, lookup=lookup, status=peakStatus)

            # Overbooking error handling.
            else:
                print("USER HAS SELECTED A DATE THAT IS ALREADY FULLY BOOKED.")
                error = "overbooked"
                return render_template('error.html', error=error)

        # Connection error handling.
        else:
            print("CANNOT CONNECT TO HH_DB")
            error = "conn"
            return render_template("error.html", error=error)

    #If user not logged in redirect to login and sign up page.
    else:
        print("USER IS NOT LOGGED IN")
        error="notLogged"
        return render_template("error.html", error=error)

# Booking confirm route
@app.route('/book_confirm/', methods=['POST', 'GET'])
def booking_confirm():
    # Check request method
    if request.method == 'POST':
        #Create variables from form
        choice = request.form['choice']
        room = request.form['room']
        confCity = request.form['city']
        checkIn = request.form['start']
        checkOut = request.form['end']
        guests = request.form['guests']
        address = request.form['address']

        #create variable for amount of nights
        nights = datetime.strptime(
            checkOut, '%Y-%m-%d') - datetime.strptime(checkIn, '%Y-%m-%d')

        #Create variable for user currency choice
        currencyChoice = request.form["paymentType"]

        #Add total fare for selected currency
        if currencyChoice == "Pounds":
            totalFare = request.form["totalFarePounds"]
        elif currencyChoice == "Euros":
            totalFare = request.form["totalFareEuros"]
        elif currencyChoice == "Dollars":
            totalFare = request.form["totalFareDollars"]

        #Create booking data list
        bookingData = [choice, room, confCity, address,
                       checkIn, checkOut, guests, totalFare, nights.days, currencyChoice]
        todaysDate = date.today()
        
        #Connect to DB
        conn = dbfunc.getConnection()
        if conn != None:
            print("CONNECTED TO DATABASE: HH_DB")
            dbcursor = conn.cursor()

            # Get users customer ID
            dbcursor.execute(
                'SELECT customerId FROM customer WHERE email = %s', (session.get('email'), ))
            loggedInCustomerId = dbcursor.fetchall()
            loggedInCustomerId = loggedInCustomerId[0][0]

            # Create booking
            dbcursor.execute('INSERT INTO bookings (customerId, roomId, dateBooked, startDate, endDate, guests, totalFare, currency) VALUES \
                (%s, %s, %s, %s, %s, %s, %s, %s);', (loggedInCustomerId, choice, todaysDate, checkIn, checkOut, guests, totalFare, currencyChoice))
            print('Booking statement executed successfully.')
            conn.commit()

            #Close connections and show completed booking
            dbcursor.close()
            conn.close()
            print("DISCONNECTED FROM HH_DB!")

            return render_template('Booking/confirm.html', resultset=bookingData)
        
        # Connection error handling.
        else:
            print("CANNOT CONNECT TO HH_DB")
            error = "conn"
            return render_template("error.html", error=error)

@app.route('/hotel-selection/', methods=['POST', 'GET'])
def hotelSel():
    # Check POST request
    if request.method == 'POST':
        #Pull hotel variable from form
        hotelSelected = request.form['hotel']

        # Connect to DB
        conn = dbfunc.getConnection()

        # Check DB connection
        if conn != None:
            print("CONNECTED TO DATABASE: HH_DB")
            dbcursor = conn.cursor()

            #Collect all data about the selected hotel.
            dataRows = []
            dbcursor.execute('SELECT * FROM hotel WHERE hotelCity = %s and roomType = "Standard";', (hotelSelected, ))
            rows = dbcursor.fetchall()
            for row in rows:
                data = list(row)
                dataRows.append(data)
            hotelData = dataRows[0]

            doubleDataRows = []
            dbcursor.execute('SELECT fare, offPeakFare, maxOccupancy FROM hotel WHERE hotelCity = %s and roomType = "Double";', (hotelSelected, ))
            doubleRows = dbcursor.fetchall()
            for row in doubleRows:
                dataDouble = list(row)
                doubleDataRows.append(dataDouble)
            doubleData = doubleDataRows[0]

            familyDataRows = []
            dbcursor.execute('SELECT fare, offPeakFare, maxOccupancy FROM hotel WHERE hotelCity = %s and roomType = "Family";', (hotelSelected, ))
            familyRows = dbcursor.fetchall()
            for row in familyRows:
                dataFamily = list(row)
                familyDataRows.append(dataFamily)
            familyData = familyDataRows[0]

            for row in doubleData:
                hotelData.append(row)
            
            for row in familyData:
                hotelData.append(row)

            # Close DB connection.
            dbcursor.close()
            conn.close()
            print("DISCONNECTED FROM HH_DB!")

            session['hotelData'] = hotelData

            return render_template('Account/edit_hotel.html', hotelData=hotelData, hotel=hotelData[2])

        # Connection error handling.
        else:
            print("CANNOT CONNECT TO HH_DB")
            error = "conn"
            return render_template("error.html", error=error)

@app.route('/edit-hotel/', methods=['POST','GET'])
def editHotel():
    # Check POST request
    if request.method == 'POST':
        newAddress = request.form['address']
        hotel = request.form['hotel']

        # Connect to DB
        conn = dbfunc.getConnection()

        # Check DB connection
        if conn != None:
            print("CONNECTED TO DATABASE: HH_DB")
            dbcursor = conn.cursor()

            #Change address
            dbcursor.execute("UPDATE hotel SET address = %s WHERE hotelCity = %s", (newAddress, hotel ))
            conn.commit()
            print(hotel + " address changed to " + newAddress)
            dbcursor.close()
            conn.close()
            print("DISCONNECTED FROM HH_DB!")

            error="update"
            return render_template('error.html', error=error)

        # Connection error handling
        else:
            print("CANNOT CONNECT TO HH_DB")
            error = "conn"
            return render_template("error.html", error=error)

@app.route('/edit-hotel-standard/', methods=['POST','GET'])
def editStandard():
    # Check POST request
    if request.method == 'POST':
        newStandardFare = request.form['standardFare']
        newStandardOffFare = request.form['standardOffFare']
        newStandardOccupancy = request.form['standardOccupancy']
        hotel = request.form['hotel']

        try:
            newStandardFare = float(newStandardFare)
            newStandardOffFare = float(newStandardOffFare)

            # Connect to DB
            conn = dbfunc.getConnection()

            #Update selected hotel with new prices and occupancy
            
            # Check DB connection
            if conn != None:
                print("CONNECTED TO DATABASE: HH_DB")
                dbcursor = conn.cursor()

                dbcursor.execute('UPDATE hotel SET fare = %s, offPeakFare = %s, maxOccupancy = %s WHERE hotelCity = %s and roomType = "Standard";', (newStandardFare, newStandardOffFare, newStandardOccupancy, hotel))
                conn.commit()

                print(hotel + " updated to have a new standard fare, standard offpeak fare and standard occupancy " + str(newStandardFare), str(newStandardOffFare), newStandardOccupancy)
                dbcursor.close()
                conn.close()
                print("DISCONNECTED FROM HH_DB!")

                error="update"
                return render_template('error.html', error=error)
            

        except ValueError:
            error = "value"
            return render_template("error.html",error=error)


@app.route('/edit-hotel-double/', methods=['POST','GET'])
def editDouble():
    # Check POST request
    if request.method == 'POST':
        newDoubleFare = request.form['doubleFare']
        newDoubleOffFare = request.form['doubleOffFare']
        newDoubleOccupancy = request.form['doubleOccupancy']
        hotel = request.form['hotel']

        try:
            newDoubleFare = float(newDoubleFare)
            newDoubleOffFare = float(newDoubleOffFare)

            # Connect to DB
            conn = dbfunc.getConnection()

            #Update selected hotel with new prices and occupancy
            
            # Check DB connection
            if conn != None:
                print("CONNECTED TO DATABASE: HH_DB")
                dbcursor = conn.cursor()

                dbcursor.execute('UPDATE hotel SET fare = %s, offPeakFare = %s, maxOccupancy = %s WHERE hotelCity = %s and roomType = "Double";', (newDoubleFare, newDoubleOffFare, newDoubleOccupancy, hotel))
                conn.commit()

                print(hotel + " updated to have a new double fare, double offpeak fare and double occupancy " + str(newDoubleFare), str(newDoubleOffFare), newDoubleOccupancy)
                dbcursor.close()
                conn.close()
                print("DISCONNECTED FROM HH_DB!")

                error="update"
                return render_template('error.html', error=error)
            

        except ValueError:
            error = "value"
            return render_template("error.html",error=error)

@app.route('/edit-hotel-family/', methods=['POST','GET'])
def editFamily():
    # Check POST request
    if request.method == 'POST':
        newFamilyFare = request.form['familyFare']
        newFamilyOffFare = request.form['familyOffFare']
        newFamilyOccupancy = request.form['familyOccupancy']
        hotel = request.form['hotel']

        try:
            newFamilyFare = float(newFamilyFare)
            newFamilyOffFare = float(newFamilyOffFare)

            # Connect to DB
            conn = dbfunc.getConnection()

            #Update selected hotel with new prices and occupancy
            
            # Check DB connection
            if conn != None:
                print("CONNECTED TO DATABASE: HH_DB")
                dbcursor = conn.cursor()

                dbcursor.execute('UPDATE hotel SET fare = %s, offPeakFare = %s, maxOccupancy = %s WHERE hotelCity = %s and roomType = "Family";', (newFamilyFare, newFamilyOffFare, newFamilyOccupancy, hotel))
                conn.commit()

                print(hotel + " updated to have a new family fare, family offpeak fare and family occupancy " + str(newFamilyFare), str(newFamilyOffFare), newFamilyOccupancy)
                dbcursor.close()
                conn.close()
                print("DISCONNECTED FROM HH_DB!")

                error="update"
                return render_template('error.html', error=error)
            

        except ValueError:
            error = "value"
            return render_template("error.html",error=error)

@app.route('/comments/', methods=['POST', 'GET'])
def comments():
    # Check request method
    if request.method == 'POST':
        #Create variables from form
        firstName = request.form['fname']
        lastName = request.form['lname']
        email = request.form['email']
        comment = request.form['comments']
        
        currentTime = datetime.now()
        

        #Connect to DB
        conn = dbfunc.getConnection()
        if conn != None:
            print("CONNECTED TO DATABASE: HH_DB")
            dbcursor = conn.cursor()

            #Execute insertion into DB
            dbcursor.execute('INSERT INTO comments (fName, lName, email, comments, timeLeft) VALUES (%s, %s, %s, %s, %s);', (firstName, lastName, email, comment, currentTime))
            print('Comment statement executed successfully.')
            conn.commit()
            #Close connections and redirect user
            dbcursor.close()
            conn.close()
            print("DISCONNECTED FROM HH_DB!")

            error="comment"

            return render_template('error.html', error=error)
        
        # Connection error handling.
        else:
            print("CANNOT CONNECT TO HH_DB")
            error = "conn"
            return render_template("error.html", error=error)

@app.route('/new-hotel/')
def createHotel():
    return render_template('/Account/new_hotel.html')

@app.route('/create-hotel-form/', methods=['POST', 'GET'])
def createHotelForm():
    # Check request method
    if request.method == 'POST':
        #Create variables from form
        newCity = request.form['city']
        newAdd = request.form['address']
        standardFare = request.form['fare']
        standardOffFare = request.form['offPeak']
        roomsAmount = request.form['rooms']

        standardFare = int(standardFare)
        standardOffFare = int(standardOffFare)
        roomsAmount = int(roomsAmount)

        #Create other variables for adding into DB
        amountStandardRooms = roomsAmount * .3
        amountDoubleRooms = roomsAmount * .5
        amountFamilyRooms = roomsAmount * .2

        doubleFare = standardFare * 1.2
        doubleOffFare = standardOffFare * 1.2

        familyFare = standardFare * 1.5
        familyOffFare = standardFare * 1.5

        standardOccupancy = 1
        doubleOccupancy = 2
        familyOccupancy = 6

        #Connect to DB
        conn = dbfunc.getConnection()
        if conn != None:
            print("CONNECTED TO DATABASE: HH_DB")
            dbcursor = conn.cursor()

            #Insert standard rooms into DB
            i=0
            while i <= amountStandardRooms:
                dbcursor.execute('INSERT INTO hotel (roomType, hotelCity, address, fare, offPeakFare, maxOccupancy)\
                    VALUES (%s, %s, %s, %s, %s, %s);', ("Standard", newCity, newAdd, standardFare, standardOffFare, standardOccupancy ))
                conn.commit()
                i += 1

            #Insert double rooms into DB    
            i=0
            while i <= amountDoubleRooms:
                dbcursor.execute('INSERT INTO hotel (roomType, hotelCity, address, fare, offPeakFare, maxOccupancy)\
                    VALUES (%s, %s, %s, %s, %s, %s);', ("Double", newCity, newAdd, doubleFare, doubleOffFare, doubleOccupancy ))
                conn.commit()
                i += 1

            #Insert family rooms into DB
            i=0
            while i <= amountFamilyRooms:
                dbcursor.execute('INSERT INTO hotel (roomType, hotelCity, address, fare, offPeakFare, maxOccupancy)\
                    VALUES (%s, %s, %s, %s, %s, %s);', ("Family", newCity, newAdd, familyFare, familyOffFare, familyOccupancy ))
                conn.commit()
                i += 1

            #Close connections and redirect user
            dbcursor.close()
            conn.close()
            print("DISCONNECTED FROM HH_DB!")

            error="hotel"
            
            return render_template("error.html", error=error)
        
        # Connection error handling.
        else:
            print("CANNOT CONNECT TO HH_DB")
            error = "conn"
            return render_template("error.html", error=error)

@app.route('/account/next-month/')
def nextMonth():
    #Create variables for the next month
    today = date.today()
    monthToday = today + relativedelta(months=1)
    nextMonth = monthToday.month
    thisYear = today.year
    startOfMonth = datetime(thisYear, nextMonth, 1)

    if nextMonth == 1 or nextMonth == 3 or nextMonth == 5 or nextMonth == 7 or nextMonth == 8 or nextMonth == 10 or nextMonth == 12:
        endOfMonth = datetime(thisYear, nextMonth, 31)
    elif nextMonth == 4 or nextMonth == 6 or nextMonth == 9 or nextMonth == 11:
        endOfMonth = datetime(thisYear, nextMonth, 30)
    else:
        endOfMonth = datetime(thisYear, nextMonth, 28)

    startOfMonth = startOfMonth.date()
    endOfMonth = endOfMonth.date()

    print(startOfMonth)
    print(endOfMonth)

    #Connect to DB
    conn = dbfunc.getConnection()
    if conn != None:
        print("CONNECTED TO DATABASE: HH_DB")
        dbcursor = conn.cursor()
        #Get all bookings from that month
        dbcursor.execute("SELECT * FROM fullbookinginfo WHERE startDate BETWEEN %s AND %s;", (startOfMonth, endOfMonth ))
        rows = dbcursor.fetchall()
        datarows = []
        for row in rows:
            data = list(row)
            datarows.append(data)

        return render_template('Account/months_report.html', bookingData=datarows, month = startOfMonth)

    # Connection error handling.
    else:
        print("CANNOT CONNECT TO HH_DB")
        error = "conn"
        return render_template("error.html", error=error)

# OTHER ROUTES YET TO BE COMPLETED.
@app.route('/info/about/')
def about():
    return render_template('/Info/About.html')

#Contact us route
@app.route('/info/contact_us/')
def contact():
    return render_template('Info/Contact_us.html')




@app.route('/info/privacy/')
def privacy():
    return render_template('Info/Privacy.html')


@app.route('/info/terms/')
def terms():
    return render_template('Info/Terms_conditions.html')


@app.route('/search/')
def search():
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)
