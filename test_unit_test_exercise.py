import pytest


@pytest.mark.parametrize("x1, y1, x2, y2, x, y", [
    (0, 0, 5, 5, 1, 1),
    (0, 0, 5, 5, 1, 9),
])
def test_line_maker(x1, y1, x2, y2, x, y):
    from unit_test_exercise import line_maker
    ans = line_maker(x1, y1, x2, y2, x)
    assert y == ans

@pytest.mark.parametrize("x1, y1, x2, y2, x, y", [
    (0, 0, 5, 5, 1, 1, True),
    (0, 0, 5, 5, 1, 9, True),
    (0, 0, 5, 5, 1, 9, False),
])
def test_point_tester(x1, y1, x2, y2, x, y, expected):
    from unit_test_exercise import point_tester
    ans = point_tester(x1, y1, x2, y2, x, y)
    assert expected == ans