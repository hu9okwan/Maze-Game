from random import randint
from models import Player

class Maze:
    def __init__(self, FILENAME):
        """ 
        Initiation of instance attributes 
        param FILENAME: The filename of the maze map
        param type: str
        """
        self._brick_space = []
        self._empty_space = []
        self._item_space = []

        f = open(FILENAME, 'r')
        line = f.readline()

        y = 0
        while line != '':
            x = 0
            for char in line:
                if char == ' ':
                    self._empty_space.append((y,x))
                elif char == 'E':
                    self._exit_space = (y,x)
                elif char == 'P':
                    self._player = Player(y, x)
                    self._player_space = (y, x)
                else:
                    self._brick_space.append((y,x))
                x += 1
            y += 1
            line = f.readline()

        f.close()
    
    def can_move_to(self, y, x):
        """
        Checks if entered coordinates are empty

        :param x: the x coordinate
        :type x: int

        :param y: the y coordinate
        :type y: int

        :return: true or false
        :return type: bool
        """
        if (y,x) in self._brick_space:
            return False
        else:
            return True


    def is_item(self, y, x):
        """
        Checks if entered coordinates contain a item

        :param x: the x coordinate
        :type x: int

        :param y: the y coordinate
        :type y: int

        :return: true or false
        :return type: bool
        """
        if (y,x) in self._item_space:
            return True
        else:
            return False


    def find_random_spot(self):
        """
        finds random spot that does not contain an X

        :return: a tuple with a line number and column number
        :return type: tuple
        """
        return self._empty_space[randint(0, len(self._empty_space)-1)]


    def spawn_item(self, num=4):
        """
        spawns item in random location

        :param num: how many items to spawn
        :type num: int
        """
        while len(self._item_space) != num:
            rand_spot = self.find_random_spot()

            if rand_spot not in self._item_space:
                self._item_space.append(rand_spot)


    def is_exit(self, y, x):
        """
        Checks if entered coordinates is the exit

        :param x: the x coordinate
        :type x: int

        :param y: the y coordinate
        :type y: int

        :return: true or false
        :return type: bool
        """
        if (y,x) == self._exit_space:
            return True
        else:
            return False


    @property
    def brick_space(self):
        return self._brick_space


    @property
    def item_space(self):
        return self._item_space


    @property
    def player_space(self):
        return self._player_space


    @property
    def player(self):
        return self._player


    @property
    def exit_space(self):
        return self._exit_space