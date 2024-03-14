from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="valli"
)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Query database for admin user
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = 'admin'")
        user = cursor.fetchone()

        if user and user[2] == password:  # user[2] corresponds to the password column in the users table
            # Redirect to admin dashboard on successful login
            return redirect(url_for('admin_dashboard'))
        else:
            # Display error message for invalid credentials
            error_message = "Invalid username or password. Please try again."
            return render_template('login.html', error_message=error_message)

    # Render login form for GET requests
    return render_template('login.html')

# Admin dashboard route
@app.route('/admin')
def admin_dashboard():
    return "Welcome, admin!"

if __name__ == "__main__":
    app.run(debug=True)
