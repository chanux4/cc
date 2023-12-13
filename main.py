import datetime
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)



@app.route('/')
@app.route('/home')
def option():
    return render_template('option.html')
currentDateTime = datetime.datetime.now()

connect = sqlite3.connect('database.db')
connect.execute(
    'CREATE TABLE IF NOT EXISTS customers (name TEXT, \
        email TEXT, city TEXT, BookingDate TIMESTAMP, phone TEXT)')

@app.route('/capture', methods=['GET', 'POST'])
def capture():
    if request.method == 'POST':
        customer_name = request.form['name']
        email = request.form['email']
        city = request.form['city']
        currentDateTime = request.form['currentDateTime']
        telephone = request.form['phone']



        with sqlite3.connect("database.db") as users:
            cursor = users.cursor()
            cursor.execute("INSERT INTO customers \
                    (name,email,city, BookingDate, phone) VALUES (?,?,?,?,?)",
                    (customer_name, email, city, currentDateTime, telephone))

            users.commit()
        return render_template("option.html")
    else:
        return render_template('capture.html')

@app.route('/customers')
def customers():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM customers')

    data = cursor.fetchall()
    return render_template("customers.html", data=data)

if __name__ == '__main__':
    app.run(debug=False)




