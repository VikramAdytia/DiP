import csv
import json


def csv2json(csv_file_path: str, json_file_path:str) -> None:
    with open(csv_file_path, 'r' , encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, dialect= 'excel')
        data = []
        for  i , row in enumerate(csv_reader):
            if i :
                access_level,user_id,name  = row
                user_data = {}
                user_data['access_level'] = int(access_level)
                user_data['user_id'] = f'{int(user_id):010}'
                user_data['name'] = name.capitalize()
                user_data['hash'] = hash((user_id,name))
                data.append(user_data)


    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data,json_file ,indent= 2 , ensure_ascii= False)

csv2json("task2.csv", "test2.json")