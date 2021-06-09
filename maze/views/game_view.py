import pygame
from views import View
from models import Maze
from models import sprites

class GameView(View):
    """ represents the game screen """
    def __init__(self, maze):
        """
        instantiates the instance's attributes
        
        :param maze: a maze instance
        :type maze: Maze
        """
        super().__init__()
        self._items = pygame.sprite.Group()
        self._walls = pygame.sprite.Group()
        self._maze = maze
        self._maze.spawn_item(4)
        self._mario = sprites.Mario(self._maze.player_space[0] * 50 + 25, self._maze.player_space[1] * 50)
        self._pipe = sprites.Pipe(self._maze.exit_space[0] * 50 + 25, self._maze.exit_space[1] * 50)
        self._clock = pygame.time.Clock()
        self._countdown = 30
        self._font = pygame.font.SysFont('Consolas', 30)


        for coord in self._maze.brick_space:
            self._walls.add(sprites.Brick(coord[0] * 50 + 25, coord[1] * 50))

        i = 0
        for coord in self._maze.item_space:
            items = [sprites.FireFlower, sprites.OneUp, sprites.Mushroom, sprites.Star]
            self._items.add(items[i](coord[0] * 50 + 25, coord[1] * 50))

            if i == 3:
                i = 0
            else:
                i += 1


    def _redisplay(self):
        """ displays the game """
        self._window.blit(self._mario.image, self._mario.rect)
        self._window.blit(self._pipe.image, self._pipe.rect)
        self._items.draw(self._window)
        self._walls.draw(self._window)

    def _redisplay_time(self, seconds):
        """ displays the remaining time left on the timer """
        self._window.blit(self._font.render(str(self.get_time(seconds)), True, (255, 255, 255)), (0, 0))

    def get_time(self, seconds):
        """ gets the remaining time on the timer """
        return (self._countdown-seconds)


    @property
    def mario(self):
        return self._mario


    @property
    def items(self):
        return self._items


    @property
    def clock(self):
        return self._clock