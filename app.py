from crypt import methods
from pydoc import render_doc
from tabnanny import check
from flask import Flask, render_template, request, url_for, jsonify, redirect, session
from datetime import datetime, date
from functools import wraps
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
    return render_template('Our_cities.html')


@app.route('/search/')
def search():
    return render_template('search.html')


@app.route('/account/login/')
def log_in():
    return render_template('Account/Log_in.html')


@app.route('/account/my_account/')
def myAccount():
    return render_template('Account/My_account.html')


@app.route('/account/no_account/')
def noAccount():
    return render_template('Account/no_account.html')


@app.route('/account/signup/')
def signup():
    return render_template('Account/Sign_up.html')


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
                print(data[0])

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
                            dbcursor .execute(
                                "SELECT fName, lName FROM customer WHERE email = %s;", (email, ))
                            data=dbcursor.fetchall()
                            dbcursor.close()

                            session['logged_in'] = True
                            session['email'] = request.form['email']
                            session['name'] = data[0][0] + " " + data[0][1]
                            print('You are now logged in!')
                            return redirect(url_for('index'))
                    else:
                        error = "Invalid credentials, please try again"

            return render_template("Account/Log_in.html", form=form, error=error)

    return render_template('Account/Log_in.html', form=form, error=error)


@app.route('/logout/')
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
        totalNights = datetime.strptime(
            end, '%Y-%m-%d') - datetime.strptime(start, '%Y-%m-%d')
        lookup = [city, start, end, noOfGuests, totalNights.days, room]

        conn = dbfunc.getConnection()
        if conn != None:
            print("CONNECTED TO DATABASE: HH_DB")
            dbcursor = conn.cursor()

            dbcursor.execute(
                'SELECT COUNT(*) FROM hotel WHERE hotelCity = %s and roomType = %s;', (city, room))
            totalRooms = dbcursor.fetchall()
            totalRooms = totalRooms[0][0]
            print(totalRooms)

            dbcursor.execute(
                'SELECT COUNT(*) FROM v WHERE startDate = %s and endDate = %s and roomType = %s and hotelCity = %s;', (start, end, room, city))
            roomsBooked = dbcursor.fetchall()
            roomsBooked = roomsBooked[0][0]
            print(roomsBooked)

            dbcursor.execute('SELECT * FROM hotel WHERE NOT EXISTS (SELECT * FROM bookings WHERE bookings.roomId = hotel.roomId and bookings.startDate = %s and bookings.endDate = %s) and hotelCity = %s and roomType = %s;', (start, end, city, room))
            rows = dbcursor.fetchall()
            datarows = []

            if roomsBooked < totalRooms:

                for row in rows:
                    data = list(row)
                    fare = (int(row[4]) * int(totalNights.days))
                    print(fare)
                    data.append(fare)
                    datarows.append(data)
                print(datarows)
                dbcursor.close()
                conn.close()

                return render_template('Booking/book.html', bookingSet=datarows, lookup=lookup)

            else:
                print("Too many rooms booked on this time already")
                return render_template('index.html')

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
        totalFare = ''
        address = ''
        nights = datetime.strptime(
            checkOut, '%Y-%m-%d') - datetime.strptime(checkIn, '%Y-%m-%d')

        if session.get('logged_in') == True:

            conn = dbfunc.getConnection()
            if conn != None:
                print("CONNECTED TO DATABASE: HH_DB")
                dbcursor = conn.cursor()
                dbcursor.execute(
                    'SELECT address, fare FROM hotel where roomId = %s;', (choice, ))
                row = dbcursor.fetchone()

                while row is not None:
                    data = list(row)
                    totalFare = (int(row[1]) * int(nights.days))
                    print(totalFare)
                    address = row[0]
                    row = dbcursor.fetchone()

                dbcursor.close()
                conn.close()

            bookingData = [choice, room, confCity, address,
                           checkIn, checkOut, guests, totalFare, nights.days]
            testDate = '2000-01-01'
            conn = dbfunc.getConnection()
            if conn != None:
                print("CONNECTED TO DATABASE: HH_DB")
                dbcursor = conn.cursor()

                dbcursor.execute(
                    'SELECT customerId FROM customer WHERE email = %s', (session.get('email'), ))
                loggedInCustomerId = dbcursor.fetchall()
                loggedInCustomerId = loggedInCustomerId[0][0]

                dbcursor.execute('INSERT INTO bookings (customerId, roomId, dateBooked, startDate, endDate, guests, totalFare) VALUES \
                    (%s, %s, %s, %s, %s, %s, %s);', (loggedInCustomerId, choice, testDate, checkIn, checkOut, guests, totalFare))
                print('Booking statement executed successfully.')
                conn.commit()

                dbcursor.close()
                conn.close()
                return render_template('Booking/confirm.html', resultset=bookingData)
            else:
                print('DB CONNECTION FAILED.')
                return redirect(url_for('index'))

        else:
            login = False
            return redirect(url_for('myAccount', login=login))


if __name__ == '__main__':
    app.run(debug=True)
