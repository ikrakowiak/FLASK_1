from flask import Flask, redirect, request, url_for, render_template

app = Flask(__name__)

@app.route('/')
def hello():
     return render_template("base.html", title="Base")

if __name__ == "__main__":
    app.run(debug=True)