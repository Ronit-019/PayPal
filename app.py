from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy in-memory user store
users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/ai')
def ai():
    return render_template('ai.html')

@app.route('/team_management')
def team_management():
    event_name = request.args.get('event', 'Unnamed Event')
    return render_template('team-management.html', event_name=event_name)

@app.route('/checklist')
def checklist():
    event_name = request.args.get('event', 'Unnamed Event')
    return render_template('checklist.html', event_name=event_name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if users.get(email) == password:
            return redirect(url_for('team_management'))  # ✅ Go to dashboard on success
        return "Invalid credentials", 401

    return render_template('login.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm-password')

        if password != confirm:
            return "Passwords do not match", 400

        if email in users:
            return "User already exists", 400

        users[email] = password
        return redirect(url_for('login'))  # 👈 redirects to login page

    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
