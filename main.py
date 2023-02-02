import json

file = open("bukhary.json", "r")
data = json.load(file)

def chapters(who, number):
    for i in range(len(data)):
        for j in range(len(data[i]["books"])):
            if data[i]["books"][j]["name"] == who:
                return data[i]["books"][j]["hadiths"][number]["info"]
            
def hadiths(chapter, number):
    for i in range(len(data)):
        for j in range(len(data[i]["books"])):
            if data[i]["books"][j]["name"] == chapter:
                return data[i]["books"][j]["hadiths"][number]["text"]
            else:
                return "Not Found"
def by(chapter, number):
    for i in range(len(data)):
        for j in range(len(data[i]["books"])):
            if data[i]["books"][j]["name"] == chapter:
                return data[i]["books"][j]["hadiths"][number]["by"]
            else:
                return "Not Found"

def hadiths_beautyfier(hadith, by, chapter):
    return "Hadith: " + hadith + "\n" + by + "\n" +"in" + chapter + "\n"

print(hadiths_beautyfier(hadiths("1. Revelation", 2), by("1. Revelation", 2), chapters("1. Revelation", 2)))
