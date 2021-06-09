import pytest
from maze.controllers import GameOverController
from maze.views import GameOverView
from web.models import Score


@pytest.fixture
def game_over_controller():
    score = Score('Hugo', 2000, "2021-04-08 20:03:23")
    return GameOverController(score)


def test_attr(game_over_controller):
    """ test to see if gameovercontroller instantiates the correct attributes """
    assert hasattr(game_over_controller, '_game_over_view')
    assert hasattr(game_over_controller, '_is_running')

    assert type(game_over_controller._game_over_view) == GameOverView

    assert game_over_controller._is_running == True
    assert game_over_controller.is_running == True

    game_over_controller.is_running = False

    assert game_over_controller._is_running == False
    assert game_over_controller.is_running == False