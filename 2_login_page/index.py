from flask import Flask, redirect, request, url_for, render_template

app = Flask(__name__)

users = {
    "alice": { "name" : "Alice", "pass": "alice123"},
    "dave": { "name" : "Dave", "pass": "dave123"},
    "eve": { "name" : "Eve", "pass": "eve123"}
}

def find_user(username, password):
    user = users.get(username)
    if user and user['pass'] == password:
        return user
    return None

if __name__ == "__main__":
    app.run(debug=True, port=3333)