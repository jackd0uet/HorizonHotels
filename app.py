from flask import Flask, render_template
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

@app.route('/test/')
def test():
    return render_template('newhomepage.html')

if __name__ == '__main__':
    app.run(debug = True)