import json

DB_PATH = "db/db.json"

def load_data():
    try:
        with open(DB_PATH, "r") as file:
            return json.load(file)
    
    except:
        return[]
    
def save_data(data):
    with open(DB_PATH, "w") as file:
        json.dump(data, file, indent=4)