from flask import Flask, render_template, request
from data import bank_bic, bank_name, bank_city

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/bics/", methods=['GET','POST'])
def get_html_bic_input():
  if request.method == 'POST':
    try:
      user_input_bic = (request.form['bic']).upper()
      name = user_input_bic
      return render_template('result.html',bank_name=bank_name(name),bank_bic=bank_bic(name), bank_city=bank_city(name))
    except Exception as e:
      return render_template('result.html', bank_name= 'bank not found', bank_bic= 'bic not found', bank_city='city not located')

if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True, use_reloader=True)