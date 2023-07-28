import random


def generate_name():
    vovels_list="аааааууууууееееееииииоооууыэюя"
    consonansts_list= "бббвввггдджжзклмнппррттсстфчхшщ"
    def gen_type(code):
        return "".join((random.choice(vovels_list if c == '0' else consonansts_list) for c in code))

    codes = ['0', '1', '01', '10' ,'010','101' ]
    types = [gen_type(code) for code in codes ]

    return ''.join(random.sample(types,3))

def validate_name():
    while True:
        name = generate_name()
        if len(name) >4 and len(name) < 7 :
            break
    return name


def fill_file(file_name="names.txt", limit=8):
    with open(file_name, mode="w", encoding="utf-8") as file:
        for _ in range(limit):
            file.write(validate_name().capitalize() + "\n")


fill_file()