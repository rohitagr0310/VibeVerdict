from flask import Flask, render_template, request, redirect, url_for
from random import randint

app = Flask(__name__)

messages = []
users = {
    'user1': {'username': 'user1', 'password': 'password1'},
    'user2': {'username': 'user2', 'password': 'password2'}
}

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    messages.append("You: " + message)
    reply = generate_reply()
    messages.append("Bot: " + reply)
    return redirect(url_for('index'))

def generate_reply():
    replies = ["That's interesting!", "Tell me more.", "I see.", "Interesting perspective."]
    return replies[randint(0, len(replies)-1)]

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            users[username] = {'username': username, 'password': password}
            return redirect(url_for('login'))
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
