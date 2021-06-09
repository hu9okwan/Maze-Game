import pytest
from maze.views import WelcomeView

@pytest.fixture
def welcome_view():
    return WelcomeView()


def test_welcome_view_attr(welcome_view):
    """ Test for instantiation of welcome_view instance's attributes """
    
    assert hasattr(welcome_view, "_welcome_text")
    assert hasattr(welcome_view, "_start_text")
    assert hasattr(welcome_view, "_redisplay")


def test_inherited_view_attr(welcome_view):
    """ Test for inherited view attribute """
    assert hasattr(welcome_view, "_window")


def test_inherited_view_method(welcome_view):
    """ Test for inherited view display method """
    assert hasattr(welcome_view, "display")

