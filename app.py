import json
import os
import subprocess
import requests
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'xxxx'
app.config['MYSQL_DB'] = 'space_invaders'
mysql = MySQL(app)


# Route for login page
@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Fetch form data
        username = request.form['username']
        password = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Check if user exists in database
        cur.execute("SELECT * FROM users WHERE username = %s AND passw = %s", (username, password))
        user = cur.fetchone()

        if user:
            # User exists, store username in session and redirect to home page
            session['username'] = username
            cur.execute("select username,score from users JOIN scores where users.id=scores.user_id ORDER BY score DESC LIMIT 5;")
            ranking_data = cur.fetchall()
            return render_template('ranking.html', ranking_data=ranking_data)
        else:
            # User doesn't exist or credentials are incorrect, render login page with error message
            return render_template("login.html", error="Invalid username or password")
    else:
        # GET request, render login page
        return render_template("login.html")

@app.route('/forgot')
def forgot_password():
    # You can render a template for the forgot password page
    return render_template('forgot.html')

@app.route("/close", methods=['POST'])
def close_page():
    return redirect(url_for('login'))


@app.route("/play_game", methods=['GET', 'POST'])
def play_game():
    if 'username' in session:
        username = session['username']
        cur = mysql.connection.cursor()
        cur.execute("SELECT score FROM scores WHERE user_id = (SELECT id FROM users WHERE username = %s)", (username,))
        highscore = cur.fetchone()[0]

        # Write the highscore to highscore.txt
        with open("highscore.txt", "w") as file:
            file.write(str(highscore))

        process = subprocess.Popen(["python", "main.py"])
        process.wait()
        return redirect(url_for('update_highscore'))

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        if user:
            cur.execute("DELETE FROM users WHERE email = %s", (email,))
            mysql.connection.commit()
            cur.close()
            message = "Your account has been successfully deleted."
            return render_template('forgot.html', message=message, redirect=True)
        else:
            message = "No user found with that email address."
            return render_template('forgot.html', message=message, redirect=False)
    else:
        return render_template('login.html')

@app.route("/update_highscore")
def update_highscore():
    # Read the new highscore from the file
    if 'username' in session:
        username = session['username']
        with open("highscore.txt", "r") as file:
            highscore = int(file.read())
        cur = mysql.connection.cursor()
        cur.execute("UPDATE scores SET score = %s WHERE user_id = (SELECT id FROM users WHERE username = %s)",
                    (highscore, username))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('login'))

    else:
        return 'User not logged in.'


# Route for signup page
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Fetch form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Check if user with the same email already exists
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cur.fetchone()

        if existing_user:
            # User with the same email already exists, render signup page with error message
            return render_template("signup.html", error="User with this email already exists")
        else:
            # Insert new user into database
            cur.execute("INSERT INTO users (username, email, passw) VALUES (%s, %s, %s)",
                        (username, email, password))
            mysql.connection.commit()

            # Redirect to login page after successful signup
            return redirect(url_for('login'))
    else:
        # GET request, render signup page
        return render_template("signup.html")


# Route for home page
@app.route("/home")
def home():
    if 'username' in session:
        return render_template("t.html")
    else:
        return redirect(url_for('login'))


# Route for logout
@app.route("/logout")
def logout():
    # Remove username from session if it exists
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
