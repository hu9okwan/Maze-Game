import pytest
from maze.views import GameOverView
from web.models import Score

@pytest.fixture
def gameoverview():
    score = Score('Hugo', 2000, "2021-04-08 20:03:23")
    return GameOverView(score)

def test_attr(gameoverview):
    """ test to see if the GameOverView class has the proper attributes and properties """
    assert hasattr(gameoverview, '_score')
    assert hasattr(gameoverview, '_win_text')
    assert hasattr(gameoverview, '_lost_text')
    assert hasattr(gameoverview, '_quit_text')
    assert hasattr(gameoverview, '_name_text')
