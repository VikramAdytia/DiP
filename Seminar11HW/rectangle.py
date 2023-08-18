class Rectangle:
    """frame for working with rectangles by input of int|float side|s and getting perimiter|square"""

    def __init__(self, side_a: float, side_b: float = None):
        """if there is none side_b rectangle taken for a square """
        self.side_a = float(side_a)
        if side_b is None:
            self.side_b = float(side_a)
        else:
            self.side_b = float(side_b)

    def get_perim(self) -> float:
        """getting perimeter"""
        return 2 * (self.side_a * self.side_b)

    def get_square(self) -> float:
        """getting square"""
        return self.side_a * self.side_b


class RectanglePro(Rectangle):
    """frame with operations with previously created rectangles"""

    def __add__(self, other):
        """override plus operation"""
        sum_of_perims: int = self.get_perim() + other.get_perim()
        side_a = float(self.side_a + other.side_a)
        side_b = float(sum_of_perims / 2 - side_a)
        return RectanglePro(side_a, side_b)

    def __sub__(self, other):
        """override minus operation"""
        if self.get_perim() < other.get_perim():
            self, other = other, self
        diff = self.get_perim() - other.get_perim()
        side_a = abs(self.side_a - other.side_b)
        side_b = diff / 2 - side_a
        return RectanglePro(side_a, side_b)

    def __eq__(self, other):
        """override = operation"""
        return self.get_square() == other.get_square()

    def __gt__(self, other):
        """override > operation"""
        return self.get_square() > other.get_square()

    def __le__(self, other):
        """override < operation"""
        return self.get_square() <= other.get_square()

    def __str__(self):
        "shows current perim and square"
        return f"We have perim ^ { self.get_perim()} and square ^ {self.get_perim()}\n "

    def __repr__(self):
        """represents current instance"""
        return f"We have perim ^ { self.get_perim()} and square ^ {self.get_perim()}\n "


rect_1 = RectanglePro(2, 3)
rect_2 = RectanglePro(5)
print(rect_1.get_perim())
print(rect_2.get_perim())

rect_sum = rect_1 + rect_2
print(rect_sum.get_perim())
print(rect_sum.side_a, rect_sum.side_b)
rect_diff = rect_1 - rect_2
print(rect_diff.get_perim())

print(rect_1.get_square())
print(rect_2.get_square())

print(rect_1 > rect_2)
print(rect_1 >= rect_2)
print(rect_1 == rect_2)
print(rect_1 < rect_2)
print(rect_1 <= rect_2)
