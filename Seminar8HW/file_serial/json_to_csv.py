import csv
import json


def json_to_csv(json_file_path:str , csv_file_path: str) -> None :
    with open(json_file_path , 'r' , encoding= "utf-8" ) as json_file :
        data = json.load(json_file)
    rows = []
    for access_level, user in data.items():
        for user_id, name in user.items():
            rows.append({'access_level': int(access_level), 'id' : int(user_id), 'name' : name})

    print(rows)

    with open(csv_file_path, 'w' , encoding= "uts-8" ) as csv_file:
        csv_dict = csv.DictWriter(csv_file, fieldnames=['access_level','user_id','name'] , dialect= 'excel_tab')
        csv_dict.writeheader()
        csv_dict.writerow()


json_to_csv("task2.json" ,"task3.csv")