from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/")
def home_page():
    return render_template('home.html')