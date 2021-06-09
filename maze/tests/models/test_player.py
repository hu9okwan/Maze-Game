import pytest
from maze.models import Player


@pytest.fixture
def player():
    """ Create a Player with 1, 1 coordinates and empty backpack """
    return Player(1,1)


def test_coords(player):
    """ Test for correct coordinate assignment """
    assert hasattr(player, "_x")
    assert hasattr(player, "_y")

    assert player.x == 1
    assert player.y == 1

    assert player._x == 1
    assert player._y == 1


def test_backpack(player):
    """ Test for existence of backpack """
    assert hasattr(player, "_backpack")


def test_move(player):
    """ Test for appropriate movement """

    # Move player left
    player.move("left")
    assert player.x == 0
    assert player._x == 0

    # Move player right
    player.move("right")
    assert player.x == 1
    assert player._x == 1

    # Move player up
    player.move("up")
    assert player.y == 0
    assert player._y == 0

    # Move player down
    player.move("down")
    assert player.y == 1
    assert player._y == 1


def test_adding_to_backpack(player):
    """ Test backpack setter to correctly add item to player's backpack """

    player.backpack = "I"
    assert player.backpack == ["I"]

    player.backpack = "A"
    assert player.backpack == ["I", "A"]

    player.backpack = "I"
    assert player.backpack == ["I", "A", "I"]