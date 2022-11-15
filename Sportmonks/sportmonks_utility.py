import json

# General functions
def save_dict(json_file, file_path):
    '''Function used to save json data'''
    # json
    with open(file_path, 'w') as file:
        json.dump(json_file, file)
        
def read_json(file_path):
    '''Function used to read json files'''
    with open(file_path, 'r') as file_loaded:
        json_data = json.load(file_loaded)
    return json_data