from flask import Flask
from flask import render_template
from flask import request
from flask import Flask, redirect, url_for, request
from markupsafe import escape
from quran_formater import *


app = Flask(__name__)

@app.route('/')
def index():
   return render_template('login.html', len = len(sourates()), sourates = sourates())

@app.route('/login',methods = ['POST', 'GET']) # Here wher we put if is a post or get request
def login():
   if request.method == 'POST':
      sourate = request.form['sourate'] 
      return render_template('index.html', titre = escape(sourate), nom_sourate = escape(sourate), sourate_texte= quran_text_ar(escape(sourate))) # Il faut toujours mettre ka fonction esacpe pour eviter les attaques
   else:
      user = request.args.get('name')
      return render_template('login.html')

if __name__ == '__main__':
   app.run(host = "0.0.0.0", port = 5000, debug = True)