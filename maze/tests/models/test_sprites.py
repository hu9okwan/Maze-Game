import pytest
from maze.models import sprites


@pytest.fixture
def mario():
    return sprites.Mario(1,2)


@pytest.fixture
def oneup():
    return sprites.OneUp(1,2)


@pytest.fixture
def fireflower():
    return sprites.FireFlower(1,2)


@pytest.fixture
def mushroom():
    return sprites.Mushroom(1,2)


@pytest.fixture
def star():
    return sprites.Star(1,2)


@pytest.fixture
def brick():
    return sprites.Brick(1,0)


@pytest.fixture
def pipe():
    return sprites.Pipe(1,2)


def test_mario(mario):
    """ test if mario has the correct instance attributes and method works correctly """
    assert hasattr(mario, 'image')
    assert hasattr(mario, 'rect')
    assert hasattr(mario, 'rect.x')
    assert hasattr(mario, 'rect.y')

    assert mario.rect.x == 2
    assert mario.rect.y == 1

    mario.update(2,1)
    assert mario.rect.x == 1
    assert mario.rect.y == 2


def test_oneup(oneup):
    """ test if oneup has the correct instance attributes and method works correctly """
    assert hasattr(oneup, '_image')
    assert hasattr(oneup, 'image')
    assert hasattr(oneup, 'rect')
    assert hasattr(oneup, 'rect.x')
    assert hasattr(oneup, 'rect.y')

    assert oneup.rect.x == 2
    assert oneup.rect.y == 1
    
    oneup.update(3,4)
    assert oneup.rect.x == 4
    assert oneup.rect.y == 3


def test_fireflower(fireflower):
    """ test if fireflower has the correct instance attributes and method works correctly """
    assert hasattr(fireflower, '_image')
    assert hasattr(fireflower, 'image')
    assert hasattr(fireflower, 'rect')
    assert hasattr(fireflower, 'rect.x')
    assert hasattr(fireflower, 'rect.y')

    assert fireflower.rect.x == 2
    assert fireflower.rect.y == 1

    fireflower.update(1,2)
    assert fireflower.rect.x == 2
    assert fireflower.rect.y == 1


def test_mushroom(mushroom):
    """ test if mushroom has the correct instance attributes and method works correctly """
    assert hasattr(mushroom, '_image')
    assert hasattr(mushroom, 'image')
    assert hasattr(mushroom, 'rect')
    assert hasattr(mushroom, 'rect.x')
    assert hasattr(mushroom, 'rect.y')

    assert mushroom.rect.x == 2
    assert mushroom.rect.y == 1

    mushroom.update(1,2)
    assert mushroom.rect.x == 2
    assert mushroom.rect.y == 1


def test_star(star):
    """ test if star has the correct instance attributes and method works correctly """
    assert hasattr(star, '_image')
    assert hasattr(star, 'image')
    assert hasattr(star, 'rect')
    assert hasattr(star, 'rect.x')
    assert hasattr(star, 'rect.y')

    assert star.rect.x == 2
    assert star.rect.y == 1
    
    star.update(2,5)
    assert star.rect.x == 5
    assert star.rect.y == 2


def test_brick(brick):
    """ test if brick has the correct instance attributes """
    assert hasattr(brick, 'image')
    assert hasattr(brick, 'rect')
    assert hasattr(brick, 'rect.x')
    assert hasattr(brick, 'rect.y')

    assert brick.rect.x == 0
    assert brick.rect.y == 1


def test_pipe(pipe):
    """ test if brick has the correct instance attributes """
    assert hasattr(pipe, 'image')
    assert hasattr(pipe, 'rect')
    assert hasattr(pipe, 'rect.x')
    assert hasattr(pipe, 'rect.y')

    assert pipe.rect.x == 2
    assert pipe.rect.y == 1