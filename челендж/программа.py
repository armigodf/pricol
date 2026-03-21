import json

data = {"каша": 90,
        "бутерброд": 50,
        "чай": 20}


def save():
    with open('price.json', "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False)
