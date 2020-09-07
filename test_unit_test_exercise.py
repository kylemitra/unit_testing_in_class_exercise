import pytest


@pytest.mark.parametrize("p1, p2, x, y", [
    ((0, 0), (5, 5), 1, 1),
    ((0, 0), (5, 5), 1, 9),
])
def test_line_maker(p1, p2, x, y):
    from unit_test_exercise import line_maker
    ans = line_maker(p1, p2, x)
    assert y == ansgit

@pytest.mark.parametrize("p1, p2, p3, expected", [
    ((0, 0), (5, 5), (1, 1), True),
    ((0, 0), (5, 5), (1, 9), True), # This is supposed to return false
    ((0, 0), (5, 5), (1, 9), False),
])
def test_point_tester(p1, p2, p3, expected):
    from unit_test_exercise import point_tester
    ans = point_tester(p1, p2, p3)
    assert expected == ans