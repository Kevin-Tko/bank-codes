from flask import Flask, render_template, request
import pandas as pd
from data import bank_bic, bank_name

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/BIC", methods=['GET','POST'])
def get_html_bic_input():
  if request.method == 'POST':
    user_input_bic = (request.form['bic']).upper()
    return render_template('home.html', bank_name=bank_name(user_input_bic),bank_bic=bank_bic(user_input_bic))

@app.route("/IBAN", methods=['POST'])
def get_html_iban_input():
  user_input_iban = request.form['iban']
  return render_template('home.html', iban_input=user_input_iban)


if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True, use_reloader=True)