import json

file = open("bukhary.json", "r")
data = json.load(file)

def chapters():
    for i in range(len(data)):
        for j in range(len(data[i]["books"])):
            print(data[i]["books"][j]["name"])
            
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
def chapter(chapter, number):
    for i in range(len(data)):
        for j in range(len(data[i]["books"])):
            if data[i]["books"][j]["name"] == chapter:
                return data[i]["books"][j]["hadiths"][number]["chapter"]
            else:
                return "Not Found"
def hadiths_beautyfier(hadith, by, chapter, number):
    return "Hadith: " + hadith + "\n" + "by" + by + "\n" +"in" + chapter + "\n" + "number" + number

print(hadiths_beautyfier(hadiths("1. Revelation", 0), by("1. Revelation", 0), chapter("1. Revelation", 0), "0"))