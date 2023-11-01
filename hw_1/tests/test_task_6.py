from bkovba.task_6 import task


def test_examples():
    assert task(42145) == 54421
    assert task(145263) == 654321
    assert task(123456789) == 987654321


def test_incorrect_input():
    try:
        task(-1)
    except ValueError:
        pass
    else:
        assert False


def test_zero():
    assert task(0) == 0


def test():
    assert task(112233) == 332211
    assert task(122233) == 332221
    assert task(155555) == 555551
    assert task(101) == 110
