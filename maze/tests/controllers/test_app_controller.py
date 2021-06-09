import pytest
from maze.controllers import AppController
from maze.controllers import WelcomeController
from maze.controllers import GameController
from maze.controllers import InputController
from maze.controllers import GameOverController


@pytest.fixture
def app_controller():
    """ Instantiate an instance of AppController """
    return AppController()


def test_welcome_controller_attr(app_controller):
    """ Test for instantiation of a welcome controller """
    assert hasattr(app_controller, "_welcome_controller")
    assert type(app_controller._welcome_controller) == WelcomeController


def test_current_controller_start(app_controller):
    """ Test for current_controller attribute and correct starting controller """
    assert hasattr(app_controller, "_current_controller")
    assert type(app_controller._current_controller) == WelcomeController


def test_switch_controller(app_controller):
    """ Test for correct switching of controller when method is called """

    # test for existence of switch_controller method
    assert hasattr(app_controller, "switch_controller")

    # start controller is WelcomeController
    assert type(app_controller._current_controller) == WelcomeController
    # current controller is switched to GameController
    app_controller.switch_controller()
    assert type(app_controller._current_controller) == GameController

    # current controller is switched to InputController
    app_controller.switch_controller()
    assert type(app_controller._current_controller) == InputController

    # current controller is switched to GameOverController
    app_controller.switch_controller()
    assert type(app_controller._current_controller) == GameOverController


def test_run(app_controller):
    """ Test if AppController has the method run """
    assert hasattr(app_controller, "run")

