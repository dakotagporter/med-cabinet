import json


def load_json():
    f = open('./static/data/cannabis.json', 'r')
    cannabis = json.load(f)

    f.close()

    return cannabis


def find_strain(strain):
    cannabis = load_json()
    
    index = 0
    for i in cannabis:
        for key, value in i.items():
            if value == strain:
                return cannabis[index]
        index += 1
