import pygame
import pygame.locals
from controllers import Controller
from controllers import WelcomeController
from controllers import GameController
from controllers import GameOverController
from controllers import InputController

class AppController(Controller):
    """ creates all four controllers and handles switching from one controller to another """
    def __init__(self):
        """ instantiates the instances attributes """
        self._welcome_controller = WelcomeController()
        self._current_controller = self._welcome_controller


    def switch_controller(self):
        """ switches from one controller onto another """
        if type(self._current_controller) == WelcomeController:
            self._current_controller = GameController()
        elif type(self._current_controller) == GameController:
            self._current_controller = InputController(self._current_controller.score)
        elif type(self._current_controller) == InputController:
            self._current_controller = GameOverController(self._current_controller.player_score)
        elif type(self._current_controller) == GameOverController:
            self._current_controller = self._welcome_controller


    def run(self):
        """ runs all four controllers """
        running = True
        pygame.key.set_repeat(1000, 1000)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    running = False
                elif event.type == pygame.locals.KEYDOWN:
                    if event.key == pygame.locals.K_ESCAPE:
                        running = False

            if self._current_controller.is_running == True:
                self._current_controller.run()
            else:
                self._current_controller.is_running = True
                self.switch_controller()

            pygame.display.update()