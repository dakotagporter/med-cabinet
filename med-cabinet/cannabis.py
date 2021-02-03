import json
import pickle


EFFECTS = pickle.load(open('./static/data/effects_list.pkl', 'rb'))
# EFFECTS = pickle.load(open('med-cabinet/static/data/effects_list.pkl', 'rb'))

ERROR = """Error: Strain Not Found.
           Please Try Again!"""

KEYS = ['Strain', 'Type', 'Rating', 'Effects', 'Flavor', 'Description']


def load_json():
    """Loads .json file into backend"""
    f = open('./static/data/cannabis.json', 'r')
    # f = open('med-cabinet/static/data/cannabis.json', 'r')
    cannabis = json.load(f)

    f.close()

    return cannabis


def search_strains(strain):
    """Search strains by name"""
    cannabis = load_json()
    strain = transfrom_query(strain)

    index = 0
    for i in cannabis:
        for key, value in i.items():
            if value == strain:
                return parse_values(cannabis[index])
        index += 1

    return ERROR


def find_index(index):
    cannabis = load_json()

    return parse_values(cannabis[index])


def query_results(effects, strain_type, prediction):
    cannabis = load_json()
    strains = []

    # if (any(elem in i['Effects'] for elem in effects))

    if strain_type:
        for i in cannabis:
            if i['Type'] == strain_type:
                strains.append(i)
    
    if effects:
        for i in cannabis:
            if (any(elem in i['Effects'] for elem in effects)):
                strains.append(i)

    if prediction:
        for i in prediction:
            

    
            


def parse_json(json):
    values = []
    for elem in json:
        values.append(parse_values(elem))

    return values


def transfrom_query(query):
    """Transform user query into correct format
       i.e. 'blue dream' -> 'Blue-Dream'"""
    query = query.title().split()

    trans_query = ""
    for word in query:
        trans_query += word + '-'
    trans_query = trans_query[:-1]

    return trans_query


def parse_values(dic):
    """Parse values from dictianry
       returned by 'search_strains()'"""
    if dic == ERROR:
        return ERROR

    values = []
    for key in KEYS:
        values.append(dic[key])

    return values
