import pytest
from maze.controllers import GameController

@pytest.fixture
def gamecontroller():
    return GameController()

def test_attr(gamecontroller):
    """ test to see if the game controller class has the proper attributes and properties """
    assert hasattr(gamecontroller, '_maze')
    assert hasattr(gamecontroller, '_game_view')
    assert hasattr(gamecontroller, '_is_running')
    assert hasattr(gamecontroller, '_start_time')
    assert hasattr(gamecontroller, '_total_time')
    assert hasattr(gamecontroller, '_score')
    assert hasattr(gamecontroller, '_count')

    assert gamecontroller.is_running
    assert gamecontroller.score == 0


def test_run(gamecontroller):
    """ test to see if game controller has the run method implemented """
    assert hasattr(gamecontroller, 'run')