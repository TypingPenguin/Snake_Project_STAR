import sys

from snake.game import score

def test_feature():
    INFINITE = sys.maxsize
    NORMAL_TIME = 60
    NORMAL_LENGTH = 32

    assert score(0, 0) == 0
    assert score(NORMAL_LENGTH, 0) == 0
    assert score(0, NORMAL_TIME) == 0
    assert score(INFINITE, INFINITE) is False
    assert score(NORMAL_LENGTH, INFINITE) < 1
    assert score(INFINITE, NORMAL_TIME) is False
    assert score(64, NORMAL_TIME) == (10610209857723 * (100 / NORMAL_TIME))
    assert score(65, NORMAL_TIME) is False
    assert score(NORMAL_LENGTH, NORMAL_TIME) == (2178309 * (100 / NORMAL_TIME))
    assert score(-5, -10) is False
