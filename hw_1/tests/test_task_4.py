from bkovba.task_4 import is_prime as task


def test_examples():
    assert not task(-1)
    assert not task(0)
    assert not task(1)
    assert task(2)


def test_true():
    assert task(37)


def test_false():
    assert not task(32)


def test_incorrect_input():
    assert not task(-37)


def test_large_true():
    assert task(2 ** 35 + 5)

    assert task(999999000001)


def test_large_false():
    assert not task(2 ** 35 + 4)
