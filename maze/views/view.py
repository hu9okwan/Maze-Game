import pygame
from abc import ABC, abstractmethod

class View(ABC):
    """ is inherited by the three views """
    def __init__(self):
        if not pygame.get_init():
            pygame.init()

        self._window = pygame.display.set_mode((650,425))


    def display(self):
        """ displays the view """
        self._window.fill((0, 0, 0))
        self._redisplay()

    @abstractmethod
    def _redisplay(self):
        """ an hook method for display method inherited by the three views """
        pass