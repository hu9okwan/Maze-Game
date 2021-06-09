import pytest 
from maze.views import GameView
from maze.models import Maze

@pytest.fixture
def gameview():
    maze = Maze("../test_maze.txt")
    return GameView(maze)

def test_attr(gameview):
    """ test to see if the game view class has the proper attributes and properties """
    assert hasattr(gameview, '_items')
    assert hasattr(gameview, '_walls')
    assert hasattr(gameview, '_maze')
    assert hasattr(gameview, '_mario')
    assert hasattr(gameview, '_pipe')
    assert hasattr(gameview, '_clock')
    assert hasattr(gameview, '_countdown')
    assert hasattr(gameview, '_font')

def test_get_time(gameview):
    """ test to see if the method get time returns the proper value """
    assert gameview.get_time(10) == 20
    assert gameview.get_time(15) == 15
    assert gameview.get_time(5) == 25

def test_methods(gameview):
    """ test to see if game view has the correct methods implemented """
    assert hasattr(gameview, '_redisplay')
    assert hasattr(gameview, '_redisplay_time')
    assert hasattr(gameview, 'get_time')