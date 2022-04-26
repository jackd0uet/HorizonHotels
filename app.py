from crypt import methods
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


app = Flask(__name__)

app.config.update(SECRET_KEY='osd(7:?[??jr??M7?H?')


@app.route('/test/')
def test():
    return render_template('base.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/our_cities/')
def ourCities():
    conn = dbfunc.getConnection()

    if conn != None:
        print("CONNECTED TO DATABASE: HH_DB")
        dbcursor = conn.cursor()

        dbcursor.execute("SELECT DISTINCT hotelCity FROM hotel;")
        cities = dbcursor.fetchall()
        data = []
        for city in cities:
            data.append(city)

    availability = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    return render_template('Our_cities.html', cities=data, availability=availability, date = False)


@app.route('/our_cities_date_form/', methods=['POST', 'GET'])
def ourCitiesDateForm():
    if request.method == 'POST':
        start = request.form['sDate']
        end = request.form['eDate']

        conn = dbfunc.getConnection()
        if conn != None:
            print("CONNECTED TO DATABASE: HH_DB")
            dbcursor = conn.cursor()

            availability = []

            dbcursor.execute("SELECT DISTINCT hotelCity FROM hotel;")
            cities = dbcursor.fetchall()
            data = []
            for city in cities:
                data.append(city)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Aberdeen";')
            aberdeenTotalRooms = dbcursor.fetchall()
            aberdeenTotalRooms = aberdeenTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Aberdeen";', (start, end, ))
            aberdeenRoomsBooked = dbcursor.fetchall()
            aberdeenRoomsBooked = aberdeenRoomsBooked[0][0]

            if aberdeenTotalRooms > aberdeenRoomsBooked:
                aberdeen = 1
            else:
                aberdeen = 0

            availability.append(aberdeen)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Belfast";')
            belfastTotalRooms = dbcursor.fetchall()
            belfastTotalRooms = belfastTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Belfast";', (start, end, ))
            belfastRoomsBooked = dbcursor.fetchall()
            belfastRoomsBooked = belfastRoomsBooked[0][0]

            if belfastTotalRooms > belfastRoomsBooked:
                belfast = 1
            else:
                belfast = 0

            availability.append(belfast)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Birmingham";')
            birminghamTotalRooms = dbcursor.fetchall()
            birminghamTotalRooms = birminghamTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Birmingham";', (start, end, ))
            birminghamRoomsBooked = dbcursor.fetchall()
            birminghamRoomsBooked = birminghamRoomsBooked[0][0]

            if birminghamTotalRooms > birminghamRoomsBooked:
                birmingham = 1
            else:
                birmingham = 0

            availability.append(birmingham)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Bristol";')
            bristolTotalRooms = dbcursor.fetchall()
            bristolTotalRooms = bristolTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Bristol";', (start, end, ))
            bristolRoomsBooked = dbcursor.fetchall()
            bristolRoomsBooked = bristolRoomsBooked[0][0]

            if bristolTotalRooms > bristolRoomsBooked:
                bristol = 1
            else:
                bristol = 0

            availability.append(bristol)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Cardiff";')
            cardiffTotalRooms = dbcursor.fetchall()
            cardiffTotalRooms = cardiffTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Cardiff";', (start, end, ))
            cardiffRoomsBooked = dbcursor.fetchall()
            cardiffRoomsBooked = cardiffRoomsBooked[0][0]

            if cardiffTotalRooms > cardiffRoomsBooked:
                cardiff = 1
            else:
                cardiff = 0

            availability.append(cardiff)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Edinburgh";')
            edinburghTotalRooms = dbcursor.fetchall()
            edinburghTotalRooms = edinburghTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Edinburgh";', (start, end, ))
            edinburghRoomsBooked = dbcursor.fetchall()
            edinburghRoomsBooked = edinburghRoomsBooked[0][0]

            if edinburghTotalRooms > edinburghRoomsBooked:
                edinburgh = 1
            else:
                edinburgh = 0

            availability.append(edinburgh)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Glasgow";')
            glasgowTotalRooms = dbcursor.fetchall()
            glasgowTotalRooms = glasgowTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Glasgow";', (start, end, ))
            glasgowRoomsBooked = dbcursor.fetchall()
            glasgowRoomsBooked = glasgowRoomsBooked[0][0]

            if glasgowTotalRooms > glasgowRoomsBooked:
                glasgow = 1
            else:
                glasgow = 0

            availability.append(glasgow)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "London";')
            londonTotalRooms = dbcursor.fetchall()
            londonTotalRooms = londonTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "London";', (start, end, ))
            londonRoomsBooked = dbcursor.fetchall()
            londonRoomsBooked = londonRoomsBooked[0][0]

            if londonTotalRooms > londonRoomsBooked:
                london = 1
            else:
                london = 0

            availability.append(london)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Manchester";')
            manchesterTotalRooms = dbcursor.fetchall()
            manchesterTotalRooms = manchesterTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Manchester";', (start, end, ))
            manchesterRoomsBooked = dbcursor.fetchall()
            manchesterRoomsBooked = manchesterRoomsBooked[0][0]

            if manchesterTotalRooms > manchesterRoomsBooked:
                manchester = 1
            else:
                manchester = 0

            availability.append(manchester)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Newcastle";')
            newcastleTotalRooms = dbcursor.fetchall()
            newcastleTotalRooms = newcastleTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Newcastle";', (start, end, ))
            newcastleRoomsBooked = dbcursor.fetchall()
            newcastleRoomsBooked = newcastleRoomsBooked[0][0]

            if newcastleTotalRooms > newcastleRoomsBooked:
                newcastle = 1
            else:
                newcastle = 0

            availability.append(newcastle)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Norwich";')
            norwichTotalRooms = dbcursor.fetchall()
            norwichTotalRooms = norwichTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Norwich";', (start, end, ))
            norwichRoomsBooked = dbcursor.fetchall()
            norwichRoomsBooked = norwichRoomsBooked[0][0]

            if norwichTotalRooms > norwichRoomsBooked:
                norwich = 1
            else:
                norwich = 0

            availability.append(norwich)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Nottingham";')
            nottinghamTotalRooms = dbcursor.fetchall()
            nottinghamTotalRooms = nottinghamTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Nottingham";', (start, end, ))
            nottinghamRoomsBooked = dbcursor.fetchall()
            nottinghamRoomsBooked = nottinghamRoomsBooked[0][0]

            if nottinghamTotalRooms > nottinghamRoomsBooked:
                nottingham = 1
            else:
                nottingham = 0

            availability.append(nottingham)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Oxford";')
            oxfordTotalRooms = dbcursor.fetchall()
            oxfordTotalRooms = oxfordTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Oxford";', (start, end, ))
            oxfordRoomsBooked = dbcursor.fetchall()
            oxfordRoomsBooked = oxfordRoomsBooked[0][0]

            if oxfordTotalRooms > oxfordRoomsBooked:
                oxford = 1
            else:
                oxford = 0

            availability.append(oxford)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Plymouth";')
            plymouthTotalRooms = dbcursor.fetchall()
            plymouthTotalRooms = plymouthTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Plymouth";', (start, end, ))
            plymouthRoomsBooked = dbcursor.fetchall()
            plymouthRoomsBooked = plymouthRoomsBooked[0][0]

            if plymouthTotalRooms > plymouthRoomsBooked:
                plymouth = 1
            else:
                plymouth = 0

            availability.append(plymouth)

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = "Swansea";')
            swanseaTotalRooms = dbcursor.fetchall()
            swanseaTotalRooms = swanseaTotalRooms[0][0]

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and hotelCity = "Swansea";', (start, end, ))
            swanseaRoomsBooked = dbcursor.fetchall()
            swanseaRoomsBooked = swanseaRoomsBooked[0][0]

            if swanseaTotalRooms > swanseaRoomsBooked:
                swansea = 1
            else:
                swansea = 0

            availability.append(swansea)

            dbcursor.close()
            conn.close()

            return render_template('Our_cities.html', cities=data, availability=availability, date = True, startDate = start, endDate = end)


@app.route('/account/login/')
def log_in():
    return render_template('Account/Log_in.html')


@app.route('/account/my_account/')
def myAccount():
    conn = dbfunc.getConnection()

    if conn != None:
        print("CONNECTED TO DATABASE: HH_DB")
        dbcursor = conn.cursor()

        dbcursor.execute(
            'SELECT * FROM FULLBOOKINGINFO WHERE customerId = %s;', (session.get('userId'), ))

        rows = dbcursor.fetchall()
        datarows = []

        for row in rows:
            data = list(row)
            datarows.append(data)

        dbcursor.execute(
            "SELECT * FROM cancelledBookings WHERE customerId = %s", (session.get('userId'), ))
        rowsTwo = dbcursor.fetchall()
        dataRowsTwo = []

        for row in rowsTwo:
            dataTwo = list(row)
            dataRowsTwo.append(dataTwo)

        dbcursor.execute(
            "SELECT COUNT(*) FROM cancelledBookings WHERE customerId = %s", (session.get('userId'), ))
        cancelledCount = dbcursor.fetchone()[0]

        dbcursor.close()
        conn.close()

        return render_template('Account/My_account.html', bookingData=datarows, cancelledData=dataRowsTwo, count=cancelledCount)
    else:
        print("NOT CONNECTED TO THE DATABASE")


@app.route('/account/modify_booking/', methods=['POST', 'GET'])
def modify():
    if request.method == 'POST':
        bookingId = request.form['modifyBooking']

        conn = dbfunc.getConnection()

        if conn != None:
            print("CONNECTED TO DATABASE: HH_DB")
            dbcursor = conn.cursor()

            dbcursor.execute(
                "SELECT * FROM bookings WHERE bookingId = %s;", (bookingId, ))
            rows = dbcursor.fetchall()
            datarows = []

            for row in rows:
                data = list(row)
                datarows.append(data)
            dbcursor.close()
            conn.close()

            todayDate = date.today()
            dateDifference = datarows[0][4] - todayDate
            dateDifference = dateDifference.days

            return render_template('Account/modifyBooking.html', bookingInfo=datarows[0], daysLeft=dateDifference)

        else:
            print("NOT CONNECTED TO THE DATABASE")


@app.route('/account/cancel_booking/', methods=['POST', 'GET'])
def cancel():
    if request.method == 'POST':
        daysBeforeBooking = int(request.form['Cancel'])
        bookingId = request.form['bookingId']
        customerId = request.form['customerId']
        roomId = request.form['roomId']
        dateBooked = request.form['dateBooked']
        startDate = request.form['startDate']
        endDate = request.form['endDate']
        guests = request.form['guests']
        totalPaid = float(request.form['totalPaid'])

        if daysBeforeBooking > 60:
            totalRefund = totalPaid
        elif daysBeforeBooking <= 60 and daysBeforeBooking > 30:
            totalRefund = totalPaid / 2
        else:
            totalRefund = 0

        todaysDate = date.today()

        conn = dbfunc.getConnection()
        if conn != None:
            print("CONNECTED TO DATABASE: HH_DB")
            dbcursor = conn.cursor()

            dbcursor.execute("INSERT INTO cancelledBookings (bookingId, customerId, roomId, dateBooked, \
            startDate, endDate, dateCancelled, guests, totalFare, totalRefunded) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (bookingId, customerId, roomId, dateBooked,
                                                                startDate, endDate, todaysDate, guests, totalPaid, totalRefund, ))
            dbcursor.execute(
                "DELETE FROM bookings WHERE bookingId = %s;", (bookingId, ))
            conn.commit()
            print("Booking cancelled!")
            dbcursor.close()
            conn.close()

            return render_template('/Account/confirm_cancel.html', bookId=bookingId, refund=totalRefund)
        else:
            print("NOT CONNECTED TO THE DATABASE")


@app.route('/account/no_account/')
def noAccount():
    return render_template('Account/no_account.html')


@app.route('/account/')
def account():
    if session.get('logged_in') == True:
        if session.get('userType') == "ADMIN":
            return redirect(url_for('adminHub'))
        else:
            return redirect(url_for('myAccount'))
    else:
        return redirect(url_for('noAccount'))


@app.route('/account/adminHub/')
def adminHub():
    conn = dbfunc.getConnection()

    if conn != None:
        print("CONNECTED TO DATABASE: HH_DB")
        dbcursor = conn.cursor()

        dbcursor.execute("SELECT DISTINCT hotelCity FROM hotel;")
        cities = dbcursor.fetchall()
        data = []
        for city in cities:
            data.append(city)

    return render_template('Account/admin.html', citiesData=data,)


@app.route('/check-bookings/', methods=['POST', 'GET'])
def check_bookings():
    error = ''
    if request.method == 'POST':
        startDate = request.form['startDate']
        endDate = request.form['endDate']
        city = request.form['hotel']

        conn = dbfunc.getConnection()

        if conn != None:
            print("CONNECTED TO DATABASE: HH_DB")
            dbcursor = conn.cursor()

            dbcursor.execute(
                "SELECT * FROM fullbookinginfo WHERE hotelCity = %s AND startDate BETWEEN %s AND %s;", (city, startDate, endDate))
            rows = dbcursor.fetchall()
            datarows = []
            for row in rows:
                data = list(row)
                datarows.append(data)

    return render_template('Account/check_bookings.html', bookingData=datarows)


@app.route('/account/signup/')
def signup():
    return render_template('Account/Sign_up.html')


@app.route('/sign-up/', methods=['POST', 'GET'])
def sign_up():
    error = ''
    if request.method == 'POST':
        firstName = request.form['fname']
        lastName = request.form['lname']
        dateOfBirth = request.form['dob']
        postcode = request.form['postcode']
        email = request.form['email']
        password = request.form['password']
        passwordConfirm = request.form['confpassword']

        if password == passwordConfirm:
            conn = dbfunc.getConnection()

            if conn != None:
                print("CONNECTED TO DATABASE: HH_DB")
                dbcursor = conn.cursor()

                hashedPassword = sha256_crypt.hash((str(password)))
                verifyQuery = "SELECT * FROM customer WHERE email = %s;"
                dbcursor.execute(verifyQuery, (email,))
                rows = dbcursor.fetchall()

                if dbcursor.rowcount > 0:
                    print("USER ALREADY EXISTS")
                    error = "This email is already in use, please login or use another email."
                    return render_template("Account/Sign_up.html", error=error)
                else:
                    dbcursor.execute('INSERT INTO customer(fName, lName, dob, postcode, \
                    email, password) VALUES (%s, %s, %s, %s, %s, %s);', (firstName,
                                                                         lastName, dateOfBirth, postcode, email, hashedPassword))
                    conn.commit()
                    print("USER CREATED SUCCESSFULLY")
                    dbcursor.close()
                    conn.close()
                    return redirect(url_for('login'))

                    # ADD REDIRECT HERE!

            else:
                print("CONNECTION TO DATABASE FAILED")
                return redirect(url_for('index'))

        else:
            alert = True
            return redirect(url_for('signup'))


@app.route('/login/', methods=['POST', 'GET'])
def login():
    form = {}
    error = ''

    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        form = request.form

        if email != None and password != None:
            conn = dbfunc.getConnection()
            if conn != None:
                print("CONNECTED TO HH_DB!")
                dbcursor = conn.cursor()
                dbcursor.execute("SELECT password FROM customer WHERE email = %s;",
                                 (email,))
                data = dbcursor.fetchone()

                if dbcursor.rowcount < 1:
                    error = "Email or password is incorrect, please try again."
                    dbcursor.close()
                    return render_template("Account/Log_in.html", error=error)
                else:
                    if sha256_crypt.verify(request.form['password'], str(data[0])):
                        conn = dbfunc.getConnection()
                        if conn != None:
                            print("CONNECTED TO HH_DB!")
                            dbcursor = conn.cursor()
                            dbcursor.execute(
                                "SELECT fName, lName, customerId, userType FROM customer WHERE email = %s;", (email, ))
                            data = dbcursor.fetchall()
                            data = data[0]
                            dbcursor.close()
                            conn.close()

                            session['logged_in'] = True
                            session['email'] = request.form['email']
                            session['name'] = data[0] + " " + data[1]
                            session['userId'] = data[2]
                            session['userType'] = data[3]
                            print('You are now logged in!')
                            return redirect(url_for('account'))
                    else:
                        error = "Invalid credentials, please try again"

            return render_template("Account/Log_in.html", form=form, error=error)

    return render_template('Account/Log_in.html', form=form, error=error)


@app.route('/account/my_account/logout/')
def logout():
    session.clear()
    logout = True
    return render_template('index.html', logout=logout)


@app.route('/book/', methods=['POST', 'GET'])
def booking():
    if request.method == 'POST':
        room = request.form['roomType']
        start = request.form['start-date']
        end = request.form['end-date']
        noOfGuests = request.form['guest-no']
        city = request.form['city']

        startDate = datetime.strptime(start, '%Y-%m-%d')
        endDate = datetime.strptime(
            end, '%Y-%m-%d')
        totalNights = endDate - startDate

        lookup = [city, start, end, noOfGuests, totalNights.days, room]

        if session.get('logged_in') == True:

            conn = dbfunc.getConnection()
            if conn != None:
                print("CONNECTED TO DATABASE: HH_DB")
                dbcursor = conn.cursor()

                dbcursor.execute(
                    'SELECT COUNT(*) FROM hotel WHERE hotelCity = %s and roomType = %s;', (city, room))
                totalRooms = dbcursor.fetchall()
                totalRooms = totalRooms[0][0]

                dbcursor.execute(
                    'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and roomType = %s and hotelCity = %s;', (start, end, room, city))
                roomsBooked = dbcursor.fetchall()
                roomsBooked = roomsBooked[0][0]

                dbcursor.execute('SELECT * FROM hotel WHERE NOT EXISTS (SELECT * FROM bookings WHERE bookings.roomId = hotel.roomId and bookings.startDate = %s and bookings.endDate = %s) and hotelCity = %s and roomType = %s;', (start, end, city, room))
                rows = dbcursor.fetchall()
                datarows = []

                dbcursor.execute(
                    'SELECT fare, offPeakFare FROM hotel WHERE roomType = "Standard" and hotelCity = %s', (city, ))
                standardRoomData = dbcursor.fetchall()
                standardRoomData = standardRoomData[0]

                peakStart = datetime(startDate.year, 4, 1)
                peakEnd = datetime(startDate.year, 10, 1)

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

                if roomsBooked < totalRooms:

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

                        fareEuros = fare * 1.2
                        fareUSD = fare * 1.6

                        data.append(fare)
                        data.append(fareEuros)
                        data.append(fareUSD)

                        datarows.append(data)
                    dbcursor.close()
                    conn.close()

                    return render_template('Booking/book.html', bookingSet=datarows, lookup=lookup, status=peakStatus)

                else:
                    print("Too many rooms booked on this time already")
                    return render_template('index.html')

        else:
            login = False
            return redirect(url_for('noAccount', login=login))
    # process args

    else:
        print("NOT CONNECTED TO THE DATABASE")
        return redirect(url_for('index'))


@app.route('/book_confirm/', methods=['POST', 'GET'])
def booking_confirm():
    if request.method == 'POST':
        choice = request.form['choice']
        room = request.form['room']
        confCity = request.form['city']
        checkIn = request.form['start']
        checkOut = request.form['end']
        guests = request.form['guests']
        address = request.form['address']

        nights = datetime.strptime(
            checkOut, '%Y-%m-%d') - datetime.strptime(checkIn, '%Y-%m-%d')

        currencyChoice = request.form["paymentType"]
        print(currencyChoice)

        if currencyChoice == "Pounds":
            totalFare = request.form["totalFarePounds"]
        elif currencyChoice == "Euros":
            totalFare = request.form["totalFareEuros"]
        elif currencyChoice == "Dollars":
            totalFare = request.form["totalFareDollars"]

        bookingData = [choice, room, confCity, address,
                       checkIn, checkOut, guests, totalFare, nights.days, currencyChoice]
        todaysDate = date.today()

        conn = dbfunc.getConnection()
        if conn != None:
            print("CONNECTED TO DATABASE: HH_DB")
            dbcursor = conn.cursor()

            dbcursor.execute(
                'SELECT customerId FROM customer WHERE email = %s', (session.get('email'), ))
            loggedInCustomerId = dbcursor.fetchall()
            loggedInCustomerId = loggedInCustomerId[0][0]

            dbcursor.execute('INSERT INTO bookings (customerId, roomId, dateBooked, startDate, endDate, guests, totalFare, currency) VALUES \
                (%s, %s, %s, %s, %s, %s, %s, %s);', (loggedInCustomerId, choice, todaysDate, checkIn, checkOut, guests, totalFare, currencyChoice))
            print('Booking statement executed successfully.')
            conn.commit()

            dbcursor.close()
            conn.close()
            return render_template('Booking/confirm.html', resultset=bookingData)
        else:
            print('DB CONNECTION FAILED.')
            return redirect(url_for('index'))


@app.route('/city/aberdeen/')
def aberdeen():
    return render_template('Cities/Aberdeen.html')


@app.route('/city/belfast/')
def belfast():
    return render_template('Cities/Belfast.html')


@app.route('/city/birmingham/')
def birmingham():
    return render_template('Cities/Birmingham.html')


@app.route('/city/bristol/')
def bristol():
    return render_template('Cities/Bristol.html')


@app.route('/city/cardiff/')
def cardiff():
    return render_template('Cities/Cardiff.html')


@app.route('/city/edinburgh/')
def edinburgh():
    return render_template('Cities/Edinburgh.html')


@app.route('/city/glasgow/')
def glasgow():
    return render_template('Cities/Glasgow.html')


@app.route('/city/london/')
def london():
    return render_template('Cities/London.html')


@app.route('/city/manchester/')
def manchester():
    return render_template('Cities/Manchester.html')


@app.route('/city/newcastle/')
def newcastle():
    return render_template('Cities/Newcastle.html')


@app.route('/city/norwich/')
def norwich():
    return render_template('Cities/Norwich.html')


@app.route('/city/nottingham/')
def nottingham():
    return render_template('Cities/Nottingham.html')


@app.route('/city/oxford/')
def oxford():
    return render_template('Cities/Oxford.html')


@app.route('/city/plymouth/')
def plymouth():
    return render_template('Cities/Plymouth.html')


@app.route('/city/swansea/')
def swansea():
    return render_template('Cities/Swansea.html')


@app.route('/info/about/')
def about():
    return render_template('/Info/About.html')


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
