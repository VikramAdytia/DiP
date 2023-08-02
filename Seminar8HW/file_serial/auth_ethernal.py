import ast
import json


#while True :
if __name__ == "__main__":
    with open("json_result.json", 'r') as sample:
        data : dict =  json.load(sample)
        print(data)
        sorted_x = sorted(data.items(), key=lambda x: x[1][1])
        print(sorted_x)
    with open("json_result.json", 'w') as sample:
        name = input("name")
        id = input("id")
        acces = input("acces")
        if id in data:
            print("fok u")
            json.dump(data, sample, indent=1)
        else:
            data.update({id : [name , acces]})
            json.dump(data, sample, indent=1)



