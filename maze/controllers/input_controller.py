import pygame
import pygame.locals
import datetime
from controllers import Controller
from views import userInputView
from web.models import ScoreManager
from web.models import Score



class InputController(Controller):
    """
    handles the user input and the user input view

    :param score: contains the score of the player
    :type score: int
    """
    def __init__(self, score):
        """ instantiates all the instance attributes """
        self._name = ""
        self._user_input_view = userInputView(self._name)
        self._is_running = True
        self._score = score
        self._date = str(datetime.datetime.now().replace(microsecond=0))


    def run(self):
        """ handles all user input for the input view """
        self._user_input_view.display()

        for event in pygame.event.get():
            if event.type == pygame.locals.KEYDOWN:
                user_input = pygame.key.name(event.key)
                if user_input == "backspace":
                    self._name = self._name[:-1]
                    self._user_input_view = userInputView(self._name)
                    self._user_input_view.display()
                elif user_input != "return":
                    self._name += event.unicode
                    self._user_input_view = userInputView(self._name)
                    self._user_input_view.display()

                elif event.key == pygame.locals.K_RETURN:
                    scoremanager = ScoreManager()
                    scoremanager.from_json()
                    self._player_score = Score(self._name, self._score, self._date)
                    scoremanager.add_score(self._player_score)
                    scoremanager.to_json()
                    self._is_running = False


    @property
    def name(self):
        return self._name


    @property
    def score(self):
        return self._score

    @property
    def player_score(self):
        return self._player_score


    @property
    def is_running(self):
        return self._is_running


    @is_running.setter
    def is_running(self, value):
        self._is_running = value

