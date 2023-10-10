import csv
import json

def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r', encoding='utf-8') as csv_file:        
        csv_reader = csv.reader(csv_file, delimiter=';')
        ids = next(csv_reader)

        data = {
            "uid_list": ids
        }

        with open(json_file, 'w', encoding='utf-8') as json_out:
            json.dump(data, json_out, indent=4)

csv_file_path = 'input.csv' 
json_file_path = 'output.json'  

csv_to_json(csv_file_path, json_file_path)