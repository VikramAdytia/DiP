import json
import os
import pickle


def pack_files(dir_path:str) ->None:
    json_files = filter(lambda  file_name:file_name[-5:] == '.json', os.listdir(dir_path))

    for json_file in json_files:
        with open( json_file , 'r' , encoding='utf-8' ) as json_reader:
            data = json.load(json_reader)
        with open(f'{json_files[:-5]}.pickle', 'wb') as pickle_file:
            pickle.dump(data,pickle_file)


pack_files()