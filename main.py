from flask import Flask, render_template, request
import pandas as pd
from data import bank_bic, bank_name, international_bank_name, internationa_bank_bic

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/Kenyan BICS", methods=['GET','POST'])
def get_html_bic_input():
  if request.method == 'POST':
    try:
      user_input_bic = (request.form['bic']).upper()
      return render_template('home.html',bank_name=bank_name(user_input_bic), bank_bic=bank_bic(user_input_bic))
    except Exception as e:
      return render_template('home.html', bank_name= 'bank not found', bank_bic= 'bic not found')

@app.route("/International BICS", methods=['GET','POST'])
def get_html_iban_input():
  if request.method == 'POST':
    try:
      user_input_iban = (request.form['iban']).upper()
      return render_template('home.html', int_bank_name= international_bank_name(user_input_iban), int_bank_bic=internationa_bank_bic(user_input_iban))
    except Exception as e:
      return render_template('home.html', int_bank_name= 'bank not found', int_bank_bic= 'bic not found')

if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True, use_reloader=True)