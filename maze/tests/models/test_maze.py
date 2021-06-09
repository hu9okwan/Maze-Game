import pytest
from maze.models import Maze

@pytest.fixture
def mazeobj():
    return Maze("../test_maze.txt")


def test_attr(mazeobj):
    """ test to see if the init functions creates all the appropriate attributes """
    assert hasattr(mazeobj, '_brick_space')
    assert hasattr(mazeobj, '_item_space')
    assert hasattr(mazeobj, '_empty_space')
    assert hasattr(mazeobj, '_player_space')
    assert hasattr(mazeobj, '_exit_space')

    assert mazeobj._empty_space == [(1,2)]
    assert mazeobj._player_space == (1,1)
    assert mazeobj._exit_space == (2,2)

    assert mazeobj.player_space == (1,1)
    assert mazeobj.exit_space == (2,2)


def test_can_move_to(mazeobj):
    """ test to see if the can move to method is returning appropriate values """
    assert mazeobj.can_move_to(1,2) == True
    assert mazeobj.can_move_to(0,0) == False


def test_spawn_item(mazeobj):
    """ test to see if item are spawning correctly """
    assert hasattr(mazeobj, 'spawn_item')
    mazeobj.spawn_item(1)
    assert mazeobj._item_space == [(1,2)]
    assert mazeobj.item_space == [(1,2)]


def test_is_item(mazeobj):
    """ test to see if entering coordinates into the is item method returns appropriate values """
    mazeobj.spawn_item(1)
    assert mazeobj.is_item(1,2) == True
    assert mazeobj.is_item(0,0) == False


def test_find_random_spot(mazeobj):
    """ test to see if the find random sport method is returning appropriate values """
    assert mazeobj.find_random_spot() == (1,2)

def test_is_exit(mazeobj):
    """ test to see if the coordinates entered into the is exit method returns whether or not the maze exit exists in that spot """
    assert mazeobj.is_exit(2,2) == True
    assert mazeobj.is_exit(0,0) == False
