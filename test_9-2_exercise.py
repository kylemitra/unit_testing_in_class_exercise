import pytest

@pytest.mark.parametrize("(x1, y1), (x2, y2), x, y", [
    ((0,0), (5,5), 1, 1),
])

def test_line_maker((x1, y1), (x2, y2), x, y):
    from 9-2_exercise.py import line_maker
    ans = line_maker((x1,y1), (x2,y2), x)
    assert y == ans

