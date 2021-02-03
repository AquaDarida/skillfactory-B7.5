class BoardException(Exception):
    pass


class OutOfBoundsException(BoardException):
    def __str__(self):
        return "Point is beyond the board."


class UsedPointException(BoardException):
    def __str__(self):
        return "You have already shoot here"


class RandShipPlacingException(BoardException):
    pass
