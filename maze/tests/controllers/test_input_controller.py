import pytest
from maze.controllers import input_controller

@pytest.fixture
def inputcontroller():
    return input_controller.InputController(20)

def test_attr(inputcontroller):
    """ test to make sure that InputController has the proper attributes """
    assert hasattr(inputcontroller, '_name')
    assert hasattr(inputcontroller, '_user_input_view')
    assert hasattr(inputcontroller, '_is_running')
    assert hasattr(inputcontroller, '_score')
    assert hasattr(inputcontroller, '_date')

    assert inputcontroller.score == 20

def test_run(inputcontroller):
    """ test to make sure InputController has correctly set up the run method """
    assert hasattr(inputcontroller, 'run')