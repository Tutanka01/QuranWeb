import json
from deep_translator import GoogleTranslator

file = open("C:\\Users\\zhiri\\Documents\\mo\\Bukhary_TEST\\Source\\jsons\\bukhary.json", "r") # Ouverture du fichier
data = json.load(file) # Lecture du fichier en format jsonsq, attention ça le donne en forme de liste de dictionnaire

def livres(): # Donne la liste des livres
    return [data[i]["books"][j]["name"] for i in range(len(data)) for j in range(len(data[i]["books"]))] # On parcourt les livres et on les met dans une liste

def chapters(who, number): # Donne le nom du chapitre
    for i in range(len(data)):
        for j in range(len(data[i]["books"])):
            if data[i]["books"][j]["name"] == who:
                return data[i]["books"][j]["hadiths"][number]["info"]
    return "Book not found"

## Donne tous les chapitres d'un livre
def list_chapters(name):
    for i in range(len(data)):
        for j in range(len(data[i]["books"])):
            if data[i]["books"][j]["name"] == name:
                ## Translate to french and return
                
                return [data[i]["books"][j]["hadiths"][k]["info"] for k in range(len(data[i]["books"][j]["hadiths"]))]
    raise ValueError("Book not found")

def hadiths(livre, chapitre): # Donne le hadith
    for i in range(len(data)):
        for j in range(len(data[i]["books"])):
            if data[i]["books"][j]["name"] == livre:
                return data[i]["books"][j]["hadiths"][chapitre]["text"]
    raise ValueError("Hadith not found")

def by(livre, chapitre): # Donne le nom de la persionne qui a rapporté le hadith
    for i in range(len(data)):
        for j in range(len(data[i]["books"])):
            if data[i]["books"][j]["name"] == livre:
                return data[i]["books"][j]["hadiths"][chapitre]["by"]
    raise ValueError("Chapter not found")

def traduction(texte): # Traduit le texte en français
    return GoogleTranslator(source='auto', target='fr').translate(texte)

def hadiths_beautyfier(hadith, chapter): # Ajoute un titre au hadith et le met en forme
    # Add a title to the hadith
    return "Hadith: " + hadith + "\n" + "\n" +"in" + chapter + "\n"

# Donne le texte du hadith selon le livre et le chapitre
def hadiths_text(livre, chapitre):
    return hadiths_beautyfier(hadiths(livre, chapitre), by(livre, chapitre))

 # Donne les auteurs des hadiths selon le livre et le chapitre