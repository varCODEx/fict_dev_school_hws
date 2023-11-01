from bkovba.task_2 import task


def test_formula():
    assert task(0) == 0
    assert task(1) == 1
    assert task(2) == 3


def test_negative():
    try:
        task(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError must be raised")
