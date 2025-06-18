from src.mathoperations import add, subtract


def test_add():
    assert add(5, 3) == 8
    assert add(-5, 3) == -2
    assert add(-5, -3) == -8
    assert add(5, -3) == 2

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-5, 3) == -8
    assert subtract(-5, -3) == -2
    assert subtract(5, -3) == 8