from bkovba.task_5 import highAndLow as task


def test_examples():
    assert task("1 2 3 4 5") == "5 1"
    assert task("1 2 -3 4 5") == "5 -3"
    assert task("1 9 3 4 -5") == "9 -5"


def test():
    assert task("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214"


def test_single_input():
    assert task("42") == "42 42"
