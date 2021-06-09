import pygame
import pygame.locals
from controllers import Controller
from views import GameOverView

class GameOverController(Controller):
    """
    represents the game over screen of the game

    :param score: the score and name of the current player
    :type score: Score
    """
    def __init__(self, score):
        """ instantiates instances attributes """
        self._game_over_view = GameOverView(score)
        self._is_running = True


    def run(self):
        """ handles all the user input and displays the screen """
        self._game_over_view.display()

        for event in pygame.event.get():
            if event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.locals.K_r:
                    self._is_running = False


    @property
    def is_running(self):
        return self._is_running


    @is_running.setter
    def is_running(self, value):
        self._is_running = value