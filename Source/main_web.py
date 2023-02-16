from flask import Flask
from flask import render_template
from flask import request
from quran_formater import quran_text_ar


from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('login.html')

@app.route('/login',methods = ['POST', 'GET']) # Here wher we put if is a post or get request
def login():
   if request.method == 'POST':
      sourate = request.form['sourate']
      return render_template('index.html', titre = sourate, nom_sourate = sourate, sourate_texte= quran_text_ar(sourate))
   else:
      user = request.args.get('name')
      return render_template('login.html')

if __name__ == '__main__':
   app.run(host = "0.0.0.0", port = "5000", debug = True)