import pytest

from hw2.triangle import classify_triangle


@pytest.mark.parametrize(
    ("a", "b", "c", "expected"),
    [
        pytest.param(1, 0, 2, "invalid", id="T1"),
        pytest.param(1, 1, 3, "invalid", id="T2"),
        pytest.param(2, 2, 2, "equilateral", id="T3"),
        pytest.param(2, 2, 3, "isosceles", id="T4"),
        pytest.param(3, 4, 5, "scalene", id="T5"),
    ],
)
def test_line_coverage(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected
