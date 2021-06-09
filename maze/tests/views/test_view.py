import pytest
from maze.views import View

@pytest.fixture
def view():
    return View()

def test_attr(view):
    """ test to see if the view class has sole attribute '_window' """
    assert hasattr(view, '_window')