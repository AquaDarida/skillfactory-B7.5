from point import Point


class Ship:
    def __init__(self, position_, length_, direction_):
        self.position = position_
        self.length = length_
        self.direction = direction_
        self.healthPoints = length_

    @property
    def coordinates(self):
        coordinates = []

        for i in range(self.length):
            _x = self.position.x
            _y = self.position.y

            if self.direction == 0:
                _x += i
            elif self.direction == 1:
                _y += i

            coordinates.append(Point(_x, _y))

        return coordinates

    def isAttacked(self, shotPos_):
        return shotPos_ in self.coordinates

