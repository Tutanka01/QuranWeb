import json

file = open("quran_fr.json", "r") # Ouverture du fichier
data = json.load(file)

def quran():
    noms = []
    for i in range(len(data["sourates"])):
        noms.append(data["sourates"][i]["nom_phonetique"])
    return noms

print(quran())
def quran2(sourate):
    for i in range(len(data["sourates"])):
        if data["sourates"][i]["nom_phonetique"] == sourate:
            for k in range(len(data["sourates"][i]["versets"])):
                print(len(data["sourates"][i]["versets"]))
                return data["sourates"][i]["versets"][k]["text"]
        else:
            raise ValueError("sourate not found")

