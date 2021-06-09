import pytest
from maze.views import userInputView

@pytest.fixture
def userinputview():
    return userInputView('Bob')

def test_attr(userinputview):
    """ test to see if the userInputView class has the proper attributes and properties """
    assert hasattr(userinputview, '_font')
    assert hasattr(userinputview, '_prompt_text')
    assert hasattr(userinputview, '_name_text')
    assert hasattr(userinputview, '_name')

def test_redisplay(gameview):
    """ test to see if userInputView has _redisplay correctly implemented """
    assert hasattr(userinputview, '_redisplay')
    