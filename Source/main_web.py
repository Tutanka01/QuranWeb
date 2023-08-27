from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from markupsafe import escape
from quran_formater import *
from hadith_formater import *
import logging

logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('accueil.html')

@app.route('/quran_accueuil')
def quran_accueuil():
    return render_template('quran.html', len=len(sourates()), sourates=sourates())

@app.route('/quran', methods=['POST', 'GET'])
def quran():
    if request.method == 'POST':
        sourate = request.form['sourate']
        return redirect(url_for('sourate', sourate=sourate))
    else:
        return render_template('quran.html')

@app.route('/sourate/<sourate>')
def sourate(sourate):
    return render_template('quran_sourates.html', audio=get_audio_path(sourate), len=len(quran_text_ar(escape(sourate))),
                           nom_sourate_arabe=nom_sourate_arabe(escape(sourate)), nom_sourate=escape(sourate),
                           sourate_texte=quran_text_ar(escape(sourate)), sourate_translation=quran_text_fr(escape(sourate)))

@app.route('/hadiths')
def hadiths():
    return render_template('hadiths.html', len=len(livres()), livres=livres())

@app.route('/hadith_livres/<livre>')
def hadith_livres(livre):
    return render_template('hadiths_livres.html', len=len(list_chapters(livre)), livre=livre, chapitres=list_chapters(livre))

@app.route('/livre/<livre>/<int:chapitre>')
def afficher_livre(livre, chapitre):
    titre_hadith = by(livre, chapitre)
    contenu_hadith = hadiths_text(livre, chapitre)
    source_hadith = by(livre, chapitre)

    return render_template('hadith.html', titre_hadith=titre_hadith, contenu_hadith=contenu_hadith, source_hadith=source_hadith)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

