import os
import json

def add_data_to_json(jsonfile):

    user_ids = set()
    if os.path.exists(jsonfile):
        with open(jsonfile , 'r' , encoding="utf-8 "):
            data = json.load(jsonfile)
            for user in data.values():
                user_ids.update(user.keys())

    else:
        data = {str(access_level) : dict() for access_level in range(1,8)}

    while True :
        name = input("name :")
        if not name :
            break
        id = input("id :")
        access_level = input("access_level :")
        if id in user_ids:
            continue
        data[access_level][id] = name
        with open(jsonfile, 'w', encoding="utf-8") as data_file:
            json.dump(data, data_file, ensure_ascii=False, indent=2)


add_data_to_json("task2.json")
