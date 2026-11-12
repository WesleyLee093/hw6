import pytest

from hw5.discount import checkout_with_discount


@pytest.mark.parametrize(
    ("prices", "is_member", "expected"),
    [
        pytest.param([400, 500], False, 960, id="T1"),
        pytest.param([500, 700], False, 1_260, id="T2"),
        pytest.param([400, 500], True, 960, id="T3"),
        pytest.param([500, 700], True, 1_140, id="T4"),
    ],
)
def test_logical_expressions(prices, is_member, expected):
    assert checkout_with_discount(prices, is_member) == expected
