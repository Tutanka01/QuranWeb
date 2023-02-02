import json

file = open("bukhary.json", "r")
data = json.load(file)

def chapters():
    for i in range(len(data)):
        for j in range(len(data[i]["books"])):
            print(data[i]["books"][j]["name"])
            
def hadiths(chapter, info):
    for i in range(len(data)):
        for j in range(len(data[i]["books"])):
            if data[i]["books"][j]["name"] == chapter:
                return data[i]["books"][j]["hadiths"][info]["text"]
            else:
                return "Not Found"

print(hadiths("The Book of Purification", 1))