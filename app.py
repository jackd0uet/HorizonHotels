from tabnanny import check
from flask import Flask, render_template, request, url_for, jsonify, redirect
import dbfunc, mysql.connector
from datetime import datetime, date

app = Flask(__name__)


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
def login():
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


@app.route('/book/', methods = ['POST', 'GET'])
def booking():
    if request.method == 'POST':
        room = request.form['roomType']
        start = request.form['start-date']
        end = request.form['end-date']
        noOfGuests = request.form['guest-no']
        city = request.form['city']
        totalNights = datetime.strptime(end, '%Y-%m-%d') - datetime.strptime(start, '%Y-%m-%d')
        lookup = [city, start, end, noOfGuests, totalNights.days, room]

        conn = dbfunc.getConnection()
        if conn != None:
            print("CONNECTED TO DATABASE: HH_DB")
            dbcursor = conn.cursor()
            dbcursor.execute('SELECT * FROM hotel WHERE hotelCity = %s;', (city, ))
            rows = dbcursor.fetchall()
            datarows=[]

            for row in rows:
                data = list(row)
                fare = (int(row[4]) * int(totalNights.days))
                print(fare)
                data.append(fare)
                datarows.append(data)
            print(datarows)    
            dbcursor.close()
            conn.close()
    
    # process args
            return render_template('Booking/book.html', bookingSet = datarows, lookup=lookup)
    else:
        print("NOT CONNECTED TO THE DATABASE")
        return redirect(url_for('index'))
@app.route ('/book_confirm/', methods = ['POST', 'GET'])
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
        nights = datetime.strptime(checkOut, '%Y-%m-%d') - datetime.strptime(checkIn, '%Y-%m-%d')

        conn = dbfunc.getConnection()
        if conn != None:
            print("CONNECTED TO DATABASE: HH_DB")
            dbcursor = conn.cursor()
            dbcursor.execute('SELECT address, fare FROM hotel where roomId = %s;', (choice, ))
            row = dbcursor.fetchone()

            while row is not None:
                data = list(row)
                totalFare = (int(row[1]) * int(nights.days))
                print(totalFare)
                address = row[0]
                row = dbcursor.fetchone()

            dbcursor.close()
            conn.close()

        bookingData = [choice, room, confCity, address, checkIn, checkOut, guests, totalFare, nights.days]
        testDate = '2000-01-01'
        conn = dbfunc.getConnection()
        if conn != None:
            print("CONNECTED TO DATABASE: HH_DB")
            dbcursor = conn.cursor()
            dbcursor.execute('INSERT INTO bookings (bookingId, customerId, roomId, dateBooked, startDate, endDate, guests, totalFare) VALUES \
				(1, 1, %s, %s, %s, %s, %s, %s);', (choice, testDate, checkIn, checkOut, guests, totalFare))
            print('Booking statement executed successfully.')
            conn.commit()

            dbcursor.close()
            conn.close()
            return render_template('Booking/confirm.html', resultset=bookingData)
        else:
            print('DB CONNECTION FAILED.')
            return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
