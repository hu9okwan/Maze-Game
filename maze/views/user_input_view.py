import pygame
from views import View

class userInputView(View):
    """
    represent screen where user enters their name

    :param name: name of the current player
    :type name: str
    """
    def __init__(self, name):
        super().__init__()
        prompt_str = "Enter your name: "
        self._font = pygame.font.SysFont("Arial", 30, True)
        self._prompt_text = self._font.render(prompt_str, True, (255, 255, 255))
        self._name_text = self._font.render(name, True, (255,255,255))
        self._name = name

    def _redisplay(self):
        """displays the user prompt screen"""
        self._window.blit(self._prompt_text, (0,0))
        self._window.blit(self._name_text, (205,0))

