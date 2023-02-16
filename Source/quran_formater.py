import json

file = open("quran_fr.json", "r") # Ouverture du fichier
data = json.load(file)

def quran_text_fr(nom): # Donne le nom du chapitre
    for i in range(0, len(data["sourates"])): # Il faut bien mettre "sourates"
        if data["sourates"][i]["nom_phonetique"] == nom:
            for k in range(len(data["sourates"][i]["versets"])):
                print(data["sourates"][i]["versets"][k]["text"] + "\n")
            
            return "Sourate not found"

print(quran_text_fr("Al-Baqara"))
