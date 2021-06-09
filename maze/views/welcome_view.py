import pygame
from views import View

class WelcomeView(View):
    """ represents the welcome screen """
    def __init__(self):
        """ instantiates the instance's attributes """
        super().__init__()
        welcome_str = "Welcome to the Maze game"
        start_str = "Press SPACE to start the game"
        font = pygame.font.SysFont("Arial", 30, True)
        self._welcome_text = font.render(welcome_str, True, (255, 255, 255))
        font = pygame.font.SysFont("Arial", 24, True)
        self._start_text = font.render(start_str, True, (255, 255, 255))



    def _redisplay(self):
        """ displays the welcome screen """
        self._window.blit(self._welcome_text, (0, 0))
        self._window.blit(self._start_text, (0, 30))