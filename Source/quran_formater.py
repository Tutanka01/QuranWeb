import json

file = open("quran_fr.json", "r", encoding='utf-8') # Ouverture du fichier
data = json.load(file)

def quran_text_fr(nom): # Donne le nom du chapitre
    sourate = ""
    for i in range(len(data["sourates"])): # Il faut bien mettre "sourates"
        if data["sourates"][i]["nom_phonetique"] == nom:
            for k in range(len(data["sourates"][i]["versets"])):
                sourate += data["sourates"][i]["versets"][k]["text"] + "\n"
            return sourate
def quran_text_ar(nom : str): # Donne le nom du chapitre
    sourate = ""
    for i in range(len(data["sourates"])): # Il faut bien mettre "sourates"
        if data["sourates"][i]["nom_phonetique"] == nom:
            print("hello")
            for k in range(len(data["sourates"][i]["versets"])):
                sourate += data["sourates"][i]["versets"][k]["text_arabe"] + "\n" 
            return sourate

def sourates(): # Donne la nom de tous les sourats en forme de liste
    sourate = []
    for i in range(len(data["sourates"])):
        sourate.append(data["sourates"][i]["nom_phonetique"])
    return sourate
