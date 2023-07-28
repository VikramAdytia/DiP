import random
from random import randint

MAX_INT = 1000
MIN_INT = -1000


def fill_file(file_name="numbers.txt", limit=5):
    with open(file_name, mode="w", encoding="utf-8") as file:
        for _ in range(limit):
            first_int: int = randint(MIN_INT, MAX_INT)
            secon_double: int = random.uniform(MIN_INT, MAX_INT)
            file.write(str(first_int) + "|" + str(secon_double) + "\n")


fill_file()
