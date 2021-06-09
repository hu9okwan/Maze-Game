from web.test.test_score import score
import pytest, datetime
from web.models import Score
from web.models import ScoreManager


@pytest.fixture
def score_manager():
    return ScoreManager()

def test_constructor():
    score_manager = ScoreManager()
    assert hasattr(score_manager, "_scores")
    assert score_manager._scores == []

def test_add_score(score_manager):
    assert hasattr(score_manager, "add_score")
    bob = Score("Bob", 2000, datetime.datetime.now().replace(microsecond=0))
    score_manager.add_score(bob)
    assert score_manager.scores == [{"name": "Bob", "score": 2000, "date": datetime.datetime.now().replace(microsecond=0)}]


def test_get_scores(score_manager):
    bob = Score("Bob", 1500, datetime.datetime.now().replace(microsecond=0))
    sam = Score("Sam", 1700, datetime.datetime.now().replace(microsecond=0))
    assert hasattr(score_manager, "get_scores")
    score_manager.add_score(bob)
    score_manager.add_score(sam)
    assert score_manager.get_scores() == [{"name": "Sam", "score": 1700, "date": datetime.datetime.now().replace(microsecond=0)}, {"name": "Bob", "score": 1500, "date": datetime.datetime.now().replace(microsecond=0)}]


def test_serialize(score_manager):
    assert hasattr(score_manager, "serialize")
    bob = Score("Bob", 1500, datetime.datetime.now().replace(microsecond=0))
    sam = Score("Sam", 1700, datetime.datetime.now().replace(microsecond=0))
    score_manager.add_score(bob)
    score_manager.add_score(sam)
    assert score_manager.serialize() == {'scores': [{'name': 'Sam', 'score': 1700, 'date': datetime.datetime.now().replace(microsecond=0)}, {'name': 'Bob', 'score': 1500, 'date': datetime.datetime.now().replace(microsecond=0)}]}