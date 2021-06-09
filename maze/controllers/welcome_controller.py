import pygame
import pygame.locals
from controllers.controller import Controller
from views.welcome_view import WelcomeView

class WelcomeController(Controller):
    """ represents the welcome screeen of the game """
    def __init__(self):
        """ instantiates the instance attributes """
        self._welcome_view = WelcomeView()
        self._is_running = True

    
    def run(self):
        """ handles all user input for the welcome screen """
        self._welcome_view.display()

        for event in pygame.event.get():
            if event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.locals.K_SPACE:
                    self._is_running = False


    @property
    def is_running(self):
        return self._is_running


    @is_running.setter
    def is_running(self, value):
        self._is_running = value