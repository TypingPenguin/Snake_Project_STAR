import sys

import run


def test_feature():
    INFINITE = sys.maxsize
    NORMAL_TIME = 32
    NORMAL_LENGTH = 60

    game = run.game_obj
    assert game.score(0, 0) == 0
    assert game.score(NORMAL_LENGTH, 0) == 0
    assert game.score(0, NORMAL_TIME) == 0
    assert game.score(INFINITE, INFINITE) == False
    assert game.score(NORMAL_LENGTH, INFINITE) > 1
    assert game.score(INFINITE, NORMAL_TIME) == False
    assert game.score(64, NORMAL_TIME) == (10610209857723 * (100 / NORMAL_TIME))
    assert game.score(65, NORMAL_TIME) == False
    assert game.score(NORMAL_LENGTH, NORMAL_TIME) == (2178309 * (100 / NORMAL_TIME))
    assert game.score(-5, -10) == False
