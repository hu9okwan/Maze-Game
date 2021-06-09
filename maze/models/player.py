class Player:
    """
    Represents an instances of Player
    """
    def __init__(self, y, x):
        self._backpack = []
        self._x = x
        self._y = y


    def move(self, direction):
        """
        move the player in the specified direction

        :param direction: the direction the player is going
        :type direction: str
        """
        if direction == 'left':
            self._x -= 1
        elif direction == 'right':
            self._x += 1
        elif direction == 'up':
            self._y -= 1
        elif direction == 'down':
            self._y += 1


    @property
    def backpack(self):
        return self._backpack


    @property
    def x(self):
        return self._x


    @property
    def y(self):
        return self._y


    @backpack.setter
    def backpack(self, item):
        self._backpack.append(item)