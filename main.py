import json

file = open("bukhary.json", "r")
data = json.load(file)

def chapters(who, number):
    for i in range(len(data)):
        for j in range(len(data[i]["books"])):
            if data[i]["books"][j]["name"] == who:
                return data[i]["books"][j]["hadiths"][number]["info"]
            return "Book not found"
        return "Hadith not found"
    
def hadiths(chapter, number):
    for i in range(len(data)):
        for j in range(len(data[i]["books"])):
            if data[i]["books"][j]["name"] == chapter:
                return data[i]["books"][j]["hadiths"][number]["text"]
    return "Not Found"

def by(chapter, number):
    for i in range(len(data)):
        for j in range(len(data[i]["books"])):
            if data[i]["books"][j]["name"] == chapter:
                return data[i]["books"][j]["hadiths"][number]["by"]
            else:
                return "Not Found"

def hadiths_beautyfier(hadith, by, chapter):
    # Add a title to the hadith
    return "Hadith: " + hadith + "\n" + by + "\n" +"in" + chapter + "\n"

# Voila comment faire pour avoir une belle sortie : 
# print(hadiths_beautyfier(hadiths("1. Revelation", 3), by("1. Revelation", 3), chapters("1. Revelation", 3)))

def main():
    Livre = input("Quel livre voulez-vous ?, le titre en entier ")
    hadith = int(input("Quel hadith voulez-vous ?, en num "))
    hadith -= 1
    return hadiths_beautyfier(hadiths(Livre, hadith), by(Livre, hadith), chapters(Livre, hadith))

print(main())