from bkovba.task_3 import findNb


def test_examples():
    assert findNb(1071225) == 45
    assert findNb(91716553919377) == -1


def test_legit():
    assert findNb(36) == 3


def test_false():
    assert findNb(35) == -1


def test_incorrect_input():
    try:
        findNb(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError must be raised")
