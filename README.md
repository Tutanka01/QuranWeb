# Bukhary_TEST
J'essaie de faire un truc sympa avec le fichier json avec la sunnah écrite par AlBukhary(ra)

# Nombre de livres :
Il y a un total de 9 volumes (livres), pour voir tous les titres : 

```python
for i in range(len(data):
        print(data[i]["name"]))
```
# Tous les chapitres : 
Il y a un total de 93 chapitre qu'on peut lister de la maniere suivante :

```
python
for i in range(len(data)):
    for j in range(len(data[i]["books"])):
        print(data[i]["books"][j]["name"])
```