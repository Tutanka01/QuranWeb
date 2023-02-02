import json

file = open("bukhary.json", "r")
data = json.load(file)

print(data[0]["books"][0]["hadiths"][0]["text"])

for i in data[0]["books"][0]["hadiths"]:
    print(i["info"])