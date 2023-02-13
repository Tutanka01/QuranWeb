# Bukhary_TEST
- J'essaie de faire un truc sympa avec le fichier json avec la sunnah écrite par AlBukhary(ra)

# Nombre de livres :
- Il y a un total de 9 volumes (livres), pour voir tous les titres : 

```python
for i in range(len(data):
        print(data[i]["name"]))
```
# Tous les chapitres : 
- Il y a un total de 93 chapitre qu'on peut lister de la maniere suivante :

```python
for i in range(len(data)):
    for j in range(len(data[i]["books"])):
        print(data[i]["books"][j]["name"])
```
# Ajout du Quran
- J'ai ajouté le quran dans un fichier json, par le moment j'ai pas d'idee de projet en tete, si vous avez des idees n'hesitez pas a me contacter :)

# Voila comment lire le fichier json
- Pour voir le nom des sourates du quran :

```python
def quran():
    noms = []
    for i in range(len(data["sourates"])):
        noms.append(data["sourates"][i]["nom_phonetique"])
    return noms
```	 