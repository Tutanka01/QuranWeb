import json
from deep_translator import GoogleTranslator

file = open("jsons/bukhary.json", "r") # Ouverture du fichier
data = json.load(file) # Lecture du fichier en format jsonsq, attention ça le donne en forme de liste de dictionnaire

def chapters(who, number): # Donne le nom du chapitre
    for i in range(len(data)):
        for j in range(len(data[i]["books"])):
            if data[i]["books"][j]["name"] == who:
                return data[i]  ["books"][j]["hadiths"][number]["info"]
            return "Book not found"
        raise ValueError("Info not found")
    
def hadiths(chapter, number): # Donne le hadith
    for i in range(len(data)):
        for j in range(len(data[i]["books"])):
            if data[i]["books"][j]["name"] == chapter:
                return data[i]["books"][j]["hadiths"][number]["text"]
    raise ValueError("hadith not found")

def by(chapter, number): # Donne le nom de la persionne qui a rapporte le hadith
    for i in range(len(data)):
        for j in range(len(data[i]["books"])):
            if data[i]["books"][j]["name"] == chapter:
                return data[i]["books"][j]["hadiths"][number]["by"]
            else:
                raise ValueError("chapter not found")
def traduction(texte): # Traduit le texte en français
    return GoogleTranslator(source='auto', target='ar').translate(texte)

def hadiths_beautyfier(hadith, by, chapter): # Ajoute un titre au hadith et le met en forme
    # Add a title to the hadith
    return "Hadith: " + hadith + "\n" + by + "\n" +"in" + chapter + "\n"

def main(): # Fonction principale qui demande à l'utilisateur ce qu'il veut et renvoie le hadith traduit
    Livre = input("Quel livre voulez-vous ?, le titre en entier : ")
    hadith = int(input("Quel hadith voulez-vous ?, en num : "))
    hadith -= 1
    try:
        return hadiths_beautyfier(traduction(hadiths(Livre, hadith)), by(Livre, hadith), chapters(Livre, hadith))
    except:
        return "Ce que vous avez saisi n'existe pas"
    
