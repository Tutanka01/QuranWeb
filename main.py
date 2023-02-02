import json

file = open("bukhary.json", "r")
data = json.load(file)

print(data[0]["books"][0]["hadiths"][0]["text"])

"""for i in data[0]["books"][0]["hadiths"]:
    print(i["info"] + "\n",i["by"]+ "\n", i["text"])
"""
"""for i in data[0]["books"]: # 0 is the first book
    print(i["name"])"""

"""for i in data[7]["books"]: # 1 is the second book
    print(i["name"])"""

for i in range(len(data)):
    print(data[i]["name"])