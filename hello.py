from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for, request

app = Flask(__name__)

@app.route('/index.html')
def index():
    
    return render_template('index.html', name=name)

       

# Route for handling the login page logic
@app.route('/')
def login():
    
    return render_template('authentication-sign-in-basic.html', error=error)

# Route for handling the login page logic
@app.route('/pages-register.html')
def register():
    
    return render_template('pages-register.html', error=error)

# Route for handling the login page logic
@app.route('/calendar.html')
def calendar():
    
    return render_template('calendar.html', error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
