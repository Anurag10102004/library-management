from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user credentials for demonstration purposes
USER_CREDENTIALS = {
    "admin": "password123",
    "user": "pass123",
    "anurag":"annu"
}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if username and password are correct
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            return redirect(url_for('index'))  # Redirect to the index page
        else:
            return "Invalid Credentials. Please try again."
    
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
