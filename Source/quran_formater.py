import json

file = open("jsons/quran_fr.json", "r", encoding='utf-8') # Ouverture du fichier
data = json.load(file)

def quran_text_fr(nom): # Donne le nom du chapitre
    sourate_lst = []
    for i in range(len(data["sourates"])): # Il faut bien mettre "sourates"
        if data["sourates"][i]["nom_phonetique"] == nom:
            for k in range(len(data["sourates"][i]["versets"])):
                sourate_lst.append(data["sourates"][i]["versets"][k]["text"])
            return sourate_lst

def quran_text_ar(nom : str): # Donne le nom du chapitre
    sourate_lst = []
    for i in range(len(data["sourates"])): # Il faut bien mettre "sourates"
        if data["sourates"][i]["nom_phonetique"] == nom:
            for k in range(len(data["sourates"][i]["versets"])): 
                sourate_lst.append(data["sourates"][i]["versets"][k]["text_arabe"])
            return sourate_lst
        
def long(fonction):
    return len(fonction)

def sourates(): # Donne la nom de tous les sourats en forme de liste
    sourate = []
    for i in range(len(data["sourates"])):
        sourate.append(data["sourates"][i]["nom_phonetique"])
    return sourate

def nom_sourate_arabe(nom): # Donne le nom de la sourate en arabe
    for i in range(len(data["sourates"])):
        if data["sourates"][i]["nom_phonetique"] == nom:
            return data["sourates"][i]["nom"]
