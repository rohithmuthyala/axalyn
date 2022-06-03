from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for, request

app = Flask(__name__)

@app.route('/index.html')
def index():
    import requests
    import xml.etree.ElementTree as ET  

    url = "http://34.133.19.239:8081/v1/_/data/messages?strictChannel=true&sortDir=DESC&limit=100&offset=0"

    payload={}
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5lY2xpcHNlLm9yZy9rYXB1YSIsImlhdCI6MTY1MzY0OTA1MiwiZXhwIjoxNjUzNjUwODUyLCJzdWIiOiJKTm1xR1kyb0pScyIsInNJZCI6ImNqTS1BMXplc3A4In0.Bq32pLXQZ6MjwWGsXxJ81NQSB0w3lPfCVNk5IGxmY0E5jmUDWu2LXHCxKQr7D87TbPAqB_c8Lr-nqU2OnE7qKCYYb09ptZ9tmG-jxwHg2SXT4_y9OkbFFho9gy53w9RIhGhZlugAsMxtfr_5kPuZDxzSnWRoyQn9AcVZlKuIVq7nMz1TyWVf4USXjN1niw5xWdlAWs0LzmT3hDRd6vJpwneARal2N_xpZ67PpBHjmHCSjthXbh5pLSFsNZ8__J9kD59IoG7lakCA4yZ69zUTxkLk38chmmHMY-ZRMYacCZheHqzKvd9FawWBptzPaAaGn9VxgadMLXAVa0Jg3N3qWyKVmKMoNW2lnkO-zFoXohpgSh6KGnSCpL2mw-uVOUxerRY2-UjGurk_8Nykj4-ktSS6qt_yAYD0fAiLXL_Fk3ch8MvyjGqdkbVJBZX1umygaNQKY_qmgZI3SLvpsV9CZfY17GDsu1q50HjHXX66A9R_JEp8AQ_UbMy-WTvxHkUtbsr2w4_dHlBLT6F6xajGAD8lHXQM_BK9dnHIvb2wD33qJlvcx0_2fcTA6bAnoKYeaYCO8kr9VI300TiTnS7hm02O76v4fJtRamhVNGz-AXDccX6kwCGpnDAizUEjf7N1pUVO62Nmsfiue6HBY2sOMNOquOPjHj795I-lTqOJuI8'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.text, 'lxml')


    web_content = soup.find('value')
    name = ['web_content']
    return render_template('index.html', name=name)

       

# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('authentication-sign-in-basic.html', error=error)

# Route for handling the login page logic
@app.route('/pages-register.html', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('pages-register.html', error=error)

# Route for handling the login page logic
@app.route('/calendar.html', methods=['GET', 'POST'])
def calendar():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('calendar.html', error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)