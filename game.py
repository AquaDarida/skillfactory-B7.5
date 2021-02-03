from player import Computer, User
from ship import Ship
from point import Point
from board import Board
from boardexception import RandShipPlacingException
import random


class Game:
    def __init__(self):
        self.size = 6

        computerBoard = self.createBoard()
        userBoard = self.createBoard()

        self.computer = Computer(computerBoard, userBoard)
        self.user = User(userBoard, computerBoard)

    def createBoard(self):

        resultBoard = None
        while resultBoard is None:
            resultBoard = self.createSeed()

        return resultBoard


    def createSeed(self):
        shipLength = [3, 2, 2, 1, 1, 1, 1]
        resultBoard = Board()
        attempt = 0
        for length in shipLength:
            while True:
                attempt += 1
                if attempt > 2000:
                   return None
                ship = Ship(Point(random.randint(0, 7), random.randint(0, 7)), length, random.randint(0, 1))
                try:
                    resultBoard.addShip(ship)
                    break
                except RandShipPlacingException:
                     pass

        resultBoard.clearPositions()
        return resultBoard

    def start(self):
        print("\t\t\t --- Welcome to the World Of Warships --- \t\t\t")
        print("Your goal is to become a king of Warships")
        print("Let's go!!!")

        print("Important information about coordinate input format")
        print("First you enter X (row)")
        print("Second you enter Y (column)")

        print("\t\t\t --- LET'S THE GAME BEGINS --- \t\t\t")

        print("Human's field: \n" + str(self.user.board))
        print("\n\t\t\t------------------------------------\n\n ")
        print("Computer's field: \n" + str(self.computer.board))
        print("\n\t\t\t------------------------------------\n ")

        while True:
            while True:
                print("Human's move now")
                if not self.user.step():
                    print("Human's field: \n" + str(self.user.board))
                    print("\n\t\t\t------------------------------------\n\n ")
                    print("Computer's field: \n" + str(self.computer.board))
                    print("\n\t\t\t------------------------------------\n\n ")
                    break

                print("Human's field: \n" + str(self.user.board))
                print("\n\t\t\t------------------------------------\n\n ")
                print("Computer's field: \n" + str(self.computer.board))
                print("\n\t\t\t------------------------------------\n\n ")

                if self.computer.board.deadShips == 7:
                    print("\t\t\t --- CONGRATULATIONS --- '\t\t\t")
                    print("\t\t\t You become a king of Warships")

                    print("Human's field: \n" + str(self.user.board))
                    print("\n\t\t\t------------------------------------\n\n ")
                    print("Computer's field: \n" + str(self.computer.board))
                    print("\n\t\t\t------------------------------------\n\n ")
                    exit(0)

                print("Human's field: \n" + str(self.user.board))
                print("\n\t\t\t------------------------------------\n\n ")
                print("Computer's field: \n" + str(self.computer.board))
                print("\n \t\t\t------------------------------------\n\n ")

            while True:
                print("Computer tries to destroy you")
                if not self.computer.step():
                    print("Human's field: \n" + str(self.user.board))
                    print("\n\t\t\t------------------------------------\n\n ")
                    print("Computer's field: \n" + str(self.computer.board))
                    print("\n\t\t\t------------------------------------\n\n ")
                    break
                print("Human's field: \n" + str(self.user.board))
                print("\n\t\t\t------------------------------------\n\n ")
                print("Computer's field: \n" + str(self.computer.board))
                print("\n\t\t\t------------------------------------\n\n ")
                if self.user.board.deadShips == 7:
                    print("\t\t\t --- DEFEAT --- '\t\t\t")
                    print("\t\t\t Computer destroyed you \t\t\t")

                    print("Human's field: \n" + str(self.user.board))
                    print("\n\t\t\t------------------------------------\n\n")
                    print("Computer's field: \n" + str(self.computer.board))
                    print("\n\t\t\t------------------------------------\n\n ")
                    exit(0)

                print("Human's field: \n" + str(self.user.board))
                print("\n\t\t\t------------------------------------\n\n ")
                print("Computer's field: \n" + str(self.computer.board))
                print("\n\t\t\t------------------------------------\n\n ")