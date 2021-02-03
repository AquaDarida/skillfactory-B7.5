from boardexception import OutOfBoundsException, UsedPointException, RandShipPlacingException
from point import Point


class Board:
    def __init__(self, flag_=False):
        self.size = 8
        self.field = [["-"] * self.size for i in range(self.size)]
        self.ships = []
        self.notAllowedPositions = []
        self.deadShips = 0
        self.aroundPositions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)]
        self.flag = flag_

    def __str__(self):
        result = " \t1\t2\t3\t4\t5\t6\t7\t8\n"

        for i in range(self.size):
            result += str(i + 1) + "\t"
            for j in range(self.size):
                result += str(self.field[i][j]) + "\t"
            result += "\n"

        if self.flag:
            result.replace("■", "0")

        return result

    def addShip(self, ship_):
        for point in ship_.coordinates:
            if not ((0 <= point.x < self.size and 0 <= point.y < self.size)) or (point in self.notAllowedPositions):
                raise RandShipPlacingException

        for point in ship_.coordinates:
            self.field[point.x][point.y] = "■"
            self.notAllowedPositions.append(point)

            for _x, _y in self.aroundPositions:
                _point = Point(point.x + _x, point.y + _y)
                if 0 <= _point.x < self.size and 0 <= _point.y < self.size and _point not in self.notAllowedPositions:
                    self.notAllowedPositions.append(_point)

        self.ships.append(ship_)

    def takeShot(self, point_):
        if not (0 <= point_.x < self.size and 0 <= point_.y < self.size):
            raise OutOfBoundsException()

        if point_ in self.notAllowedPositions:
            raise UsedPointException()

        self.notAllowedPositions.append(point_)

        for ship in self.ships:
            if point_ in ship.coordinates:
                ship.healthPoints -= 1
                self.field[point_.x][point_.y] = "X"
                if ship.healthPoints == 0:
                    self.deadShips += 1
                    for _point in ship.coordinates:
                        for _x, _y in self.aroundPositions:
                            point = Point(_point.x + _x, _point.y + _y)
                            if 0 <= point.x < self.size and 0 <= point.y < self.size \
                                    and point not in self.notAllowedPositions:
                                self.field[point.x][point.y] = "."
                    print("Ship was destroyed!!!")
                    return True
                else:
                    print("Ship was injured!!!")
                    return True

        self.field[point_.x][point_.y] = "T"
        print("Miss..")

        return False

    def clearPositions(self):
        self.notAllowedPositions = []
