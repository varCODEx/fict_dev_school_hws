from bkovba.task_1 import task


def test_neg():
    assert task(-1) == 0


def test_z():
    assert task(0) == 0


def test_task():
    assert task(1) == 0
    assert task(2) == 0
    assert task(3) == 0
    assert task(4) == 3
    assert task(10) == 23
    assert task(11) == 33
    assert task(12) == 33
    assert task(13) == 45
