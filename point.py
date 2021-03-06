class Point:
    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"
