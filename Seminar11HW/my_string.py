import time


class MyString(str):
    """If you use string, this class also show you creator's name and time of creating a string"""

    def __new__(cls, text: str, creator: str):
        """ Gives extra info about your string"""

        print('New started')

        instance = super().__new__(cls, text)
        instance.creator = creator
        instance.time = time.time()
        return instance

    def __str__(self):
        """Shows not only text < but also creator's name and time of creating"""

        return f"{super().__str__()} created by: {self.creator} at {self.time}"


example_1 = MyString('text1', "name1")
example_2 = MyString('text2', "name2")

print(example_1)
print(example_2)
