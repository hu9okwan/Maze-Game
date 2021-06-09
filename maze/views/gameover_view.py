import pygame
from views import View
from web.models import Score


class GameOverView(View):
    """ represents the game over screen """
    def __init__(self, score):
        """
        instantiates the instance's attributes

        :param score: name and score of the player
        :type score: Score
        """
        super().__init__()
        win_str = "Congratulations! You win."
        lost_str = "Boo hoo! You lose."
        quit_str = "Press ESCAPE to quit the game or R to restart the game"
        font = pygame.font.SysFont("Arial", 30, True)
        self._score = score
        self._win_text = font.render(win_str, True, (255, 255, 255))
        self._lost_text = font.render(lost_str, True, (255, 255, 255))
        font = pygame.font.SysFont("Arial", 24, True)
        self._quit_text = font.render(quit_str, True, (255, 255, 255))
        self._name_text = font.render(f'{self._score.player_name}: {self._score.score}', True, (255,255,255))


    def _redisplay(self):
        """ displays the game over screen """
        if self._score.score > 0:
            self._window.blit(self._win_text, (0, 0))
        else:
            self._window.blit(self._lost_text, (0, 0))
        self._window.blit(self._quit_text, (0, 30))
        self._window.blit(self._name_text, (0,50))