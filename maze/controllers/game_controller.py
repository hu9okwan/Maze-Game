# from web.models.scores import Score
import pygame
import pygame.locals
import time
from controllers import Controller
from views import GameView
from models import Maze
import os

class GameController(Controller):
    """ handles all input when in the game screen """
    def __init__(self):
        """ instantiates instances attributes """
        self._maze = Maze('maze.txt')
        self._game_view = GameView(self._maze)
        self._is_running = True
        self._start_time=time.time()
        self._total_time = 30
        self._score = 0
        self._game_view.clock.tick(1)
        self._count = 0


    def run(self):
        """ handles movement along with the inputs of the user """
        self._game_view.display()
        self._time_passed = time.time()-self._start_time

        for event in pygame.event.get():
            if event.type== pygame.KEYDOWN:
                if event.key == pygame.locals.K_w and self._maze.can_move_to(self._maze.player.y - 1, self._maze.player.x):
                    self._maze.player.move('up')
                elif event.key == pygame.locals.K_a and self._maze.can_move_to(self._maze.player.y, self._maze.player.x - 1):
                    self._maze.player.move('left')
                elif event.key == pygame.locals.K_s and self._maze.can_move_to(self._maze.player.y + 1, self._maze.player.x):
                    self._maze.player.move('down')
                elif event.key == pygame.locals.K_d and self._maze.can_move_to(self._maze.player.y, self._maze.player.x + 1):
                    self._maze.player.move('right')

                self._game_view.mario.update(self._maze.player.y * 50 + 25, self._maze.player.x * 50)

        self._game_view._redisplay_time(round(self._time_passed))

        if pygame.sprite.spritecollide(self._game_view.mario, self._game_view.items, dokill=False):
            item = pygame.sprite.spritecollide(self._game_view.mario, self._game_view.items, dokill=False)
            item[len(item) - 1].update(0, 625 - (self._count * 25))
            self._maze.player.backpack = 'I'
            self._count += 1

        if self._maze.is_exit(self._maze.player.y, self._maze.player.x) and len(self._maze.player.backpack) == len(self._maze.item_space):
            self.calculate_score()
            self._is_running = False
        elif self._maze.is_exit(self._maze.player.y, self._maze.player.x):
            self._is_running = False

        if self._game_view.get_time(round(self._time_passed)) == 0:
            self._is_running = False


    def calculate_score(self):
        """Calculates score based on time taken to collect all items and exit maze"""
        self._score = int((self._total_time - self._time_passed ) * 100)


    @property
    def is_running(self):
        return self._is_running


    @property
    def score(self):
        return self._score


    @is_running.setter
    def is_running(self, value):
        self._is_running = value