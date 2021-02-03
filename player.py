from abc import ABC
from point import Point
import random

from boardexception import BoardException


class Player:
    def __init__(self, board_, enemy_):
        self.board = board_
        self.enemy = enemy_

    def request(self):
        raise NotImplementedError()

    def step(self):
        while True:
            try:
                response = self.enemy.takeShot(self.request())
                return response
            except BoardException as ex:
                print(ex)


class Computer(Player):

    def request(self):
        point = Point(random.randint(0, 7), random.randint(0, 7))
        print(f"Computer shots to {point.x + 1} {point.y + 1}")
        return point


class User(Player):

    def request(self):
        while True:
            coordinates = input("Enter coordinates: ").split()

            if len(coordinates) != 2:
                print("Invalid coordinates amount!")
                continue

            if not coordinates[0].isdigit() or not coordinates[1].isdigit():
                print("It's not numbers :/")
                continue

            return Point(int(coordinates[0]) - 1, int(coordinates[1]) - 1)
