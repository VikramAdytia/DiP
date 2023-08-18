import csv
import pickle


def pickle2csv(pickle_file_path:str, csv_file_path:str) -> None:
    with open(pickle_file_path , 'rb' ) as pickle_file:
        data = pickle.load(pickle_file)
    headers = data[0].keys()
    with open(csv_file_path, 'w' , encoding='utf-8') as csv_file:
        csv_wirter = csv.DictWriter(csv_file,fieldnames=headers , dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        csv_wirter.writeheader()
        csv_wirter.writerow()


pickle2csv('task2.pickle', "rectangle.py.csv")