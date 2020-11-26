def add(a, b):
    return a + b + c


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'

def test_raw(q,w):
    assert sum(range(1,100,1) < 3000
