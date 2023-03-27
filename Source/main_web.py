from flask import Flask
from flask import render_template
from flask import request
from flask_cors import CORS
from flask import Flask, redirect, url_for, request
from markupsafe import escape
from quran_formater import *
from hadith_formater import *

app = Flask(__name__)
CORS(app)

@app.route('/')# La route principale cad l'ip
def index():
   return render_template('login.html', len = len(sourates()), sourates = sourates())

@app.route('/login',methods = ['POST', 'GET']) # Here wher we put if is a post or get request
def login():
   if request.method == 'POST':
      sourate = request.form['sourate'] 
      return redirect(url_for('sourate', sourate = sourate)) # On redirige vers la page sourate avec le nom de la sourate
   else:
      return render_template('index.html')

@app.route('/sourate/<sourate>')
def sourate(sourate):
   return render_template('index.html', titre = escape(sourate), nom_sourate = escape(sourate), sourate_texte= quran_text_ar(escape(sourate)))
# Possibilite de voir les hadiths...
@app.route('/hadith')
def hadith():
   return render_template('hadith.html')

if __name__ == '__main__':
   app.run(host = "0.0.0.0", port = 5000, debug = True)