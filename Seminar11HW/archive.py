class Archive:
    """
    Keeps a pair of params
    """

    _instance = None

    def __init__(self, text: str, num: int):
        """self explaining """
        print("init")
        self.text = text
        self.num = num

    def __new__(cls, *args, **kwargs):
        """
        Adding strings and nums to archive
        """
        print("new")
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.nums_archive = []
            cls._instance.text_archive = []
        else:
            cls._instance.nums_archive.append(cls._instance.num)
            cls._instance.text_archive.append(cls._instance.text)
        return cls._instance

    def __str__(self):
        "shows current archive instance and lists of previous"
        return f"We have text ^ { self.text} and number ^ {self.num}\n " \
               f"Archive of text : {Archive._instance.text_archive} \n " \
               f"Archive of nums : {Archive._instance.nums_archive} "

    def __repr__(self):
        """represents current instance"""
        return f"We have text ^ { self.text} and number ^ {self.num}\n "



elem_1 = Archive('text1', 11)
elem_2 = Archive('text2', 22)
elem_3 = Archive('text3', 33)

print(Archive._instance.nums_archive)
print(elem_1._instance)

print(elem_1)