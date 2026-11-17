from itertools import product

import pytest

from hw6.function_xy import F

X_VALUES = (-1, 0, 1, 2, 3)
Y_VALUES = (10, 20, 30)
# A literal oracle table, independent of the implementation's branches.
EXPECTED = {
    -1: {10: -1, 20: -2, 30: -3},
    0: {10: 0, 20: 0, 30: 0},
    1: {10: 1, 20: 2, 30: 3},
    2: {10: 2, 20: 4, 30: 6},
    3: {10: 3, 20: 6, 30: 9},
}
CATEGORIZATION = ((-1, 10), (0, 20), (1, 30), (2, 10), (3, 20))
COMBINATIONS = tuple(product(X_VALUES, Y_VALUES))
# Two observation passes over 15 input pairs; NOT 30 distinct input pairs.
OBSERVATIONS = tuple(product(("X", "Y"), X_VALUES, Y_VALUES))


@pytest.mark.parametrize("x,y", CATEGORIZATION, ids=[f"XY-CAT{i}" for i in range(1, 6)])
def test_xy_categorization(x, y):
    assert F(x, y) == EXPECTED[x][y]


@pytest.mark.parametrize("x,y", COMBINATIONS,
                         ids=[f"XY-COM{i:02d}" for i in range(1, 16)])
def test_xy_combinations(x, y):
    assert F(x, y) == EXPECTED[x][y]


@pytest.mark.parametrize("focus,x,y", OBSERVATIONS,
                         ids=[f"OBS-{focus}-{x}-{y}" for focus, x, y in OBSERVATIONS])
def test_xy_lecture_30_observations(focus, x, y):
    actual = F(x, y)
    assert actual == EXPECTED[x][y]
    if focus == "X":
        # X controls the sign / zero property of the result.
        assert (actual > 0) - (actual < 0) == (x > 0) - (x < 0)
    else:
        # Y linearly scales the value relative to the independently tabulated y=10 value.
        assert actual * 10 == EXPECTED[x][10] * y


def test_xy_design():
    assert len(CATEGORIZATION) == 5
    assert {x for x, _ in CATEGORIZATION} == set(X_VALUES)
    assert {y for _, y in CATEGORIZATION} == set(Y_VALUES)
    assert len(COMBINATIONS) == len(set(COMBINATIONS)) == 15
    assert set(COMBINATIONS) == {(x, y) for x in X_VALUES for y in Y_VALUES}
    assert len(OBSERVATIONS) == len(set(OBSERVATIONS)) == 30
    assert {(x, y) for _, x, y in OBSERVATIONS} == set(COMBINATIONS)
    assert {focus for focus, _, _ in OBSERVATIONS} == {"X", "Y"}
