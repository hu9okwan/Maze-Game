import pytest, datetime
from web.models import Score


@pytest.fixture # Defines the following function as a fixture
def score():
	return Score("Bob", 2000, datetime.datetime.now().replace(microsecond=0))

def test_constructor():
    with pytest.raises(ValueError):
        bad_score = Score("Bob", "score", datetime.datetime.now().replace(microsecond=0))
    
    with pytest.raises(ValueError):
        bad_name = Score(500, 2000, datetime.datetime.now().replace(microsecond=0))

    with pytest.raises(ValueError):
        bad_date = Score("Bob", 2000, "2021-04-03")


def test_name(score):

    assert hasattr(score, "_player_name")
    assert type(score.__class__.player_name) == property
    assert score._player_name == "Bob"

def test_score(score):

    assert hasattr(score, "_score")
    assert type(score.__class__.score) == property
    assert score._score == 2000

def test_date(score):
    assert hasattr(score, "_date")
    assert score._date == datetime.datetime.now().replace(microsecond=0)