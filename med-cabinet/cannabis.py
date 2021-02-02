import json


EFFECTS = ['Creative', 'Energetic', 'Euphoric', 
           'Focused', 'Giggly', 'Happy', 
           'Hungry', 'Relaxed', 'Sleepy', 
           'Talkative', 'Tingly', 'Uplifted']

ERROR = """Error: Strain Not Found.
           Please Try Again!"""

VALUES = []


def load_json():
    """Loads .json file into backend"""
    f = open('./static/data/cannabis.json', 'r')
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
    
    keys = ['Strain', 'Type', 'Rating', 'Effects', 'Flavor', 'Description']
    values = []
    for key in keys:
        values.append(dic[key])

    return values

