import pytest
from maze.controllers import WelcomeController
from maze.views import WelcomeView

@pytest.fixture
def welcome_controller():
    return WelcomeController()


def test_welcome_controller_attr(welcome_controller):
    """ Test for instantiation of a welcome view """
    assert hasattr(welcome_controller, "_welcome_view")
    assert type(welcome_controller._welcome_view) == WelcomeView


def test_if_running(welcome_controller):
    """ Test to check if is_running attribute is set to True on instantiation """
    assert hasattr(welcome_controller, "is_running")
    
    assert welcome_controller._is_running == True
    # test using property
    assert welcome_controller.is_running == True


def test_is_running_attr(welcome_controller):
    """ Test reassignment of is_running attribute using setter """
    welcome_controller.is_running = False
    assert welcome_controller.is_running == False

