import pygame
from abc import ABC, abstractmethod

class Controller(ABC):
    """ is inherited by the four controllers """
    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        """ an abstract method that is inherited by all controllers """
        pass