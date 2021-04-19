

# Route for handling the login page logic
from flask import Flask, render_template, request, session, flash
import os

app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'Login Successful! Welcome to BITS Work Integrated Learning Programme!'


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == '2020ht66546':
        session['logged_in'] = True
        return home()
    else:
        flash('Login failed due to incorrect Username or Password!')


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
