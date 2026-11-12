import pytest

from hw4.checkout import checkout_total


@pytest.mark.parametrize(
    ("prices", "expected"),
    [
        pytest.param([10], 10, id="T1"),
        pytest.param([500] * 100, 50_000, id="T2"),
    ],
)
def test_valid_extremes(prices, expected):
    assert checkout_total(prices) == expected


@pytest.mark.parametrize(
    ("prices", "message"),
    [
        pytest.param("10", "prices must be a list", id="T3"),
        pytest.param([], "at least 1 item is required", id="T4"),
        pytest.param([10] * 101, "at most 100 items are allowed", id="T5"),
        pytest.param([10.5], "price must be an integer", id="T6"),
        pytest.param([9], "price must be at least 10", id="T7"),
        pytest.param([501], "price must be at most 500", id="T8"),
    ],
)
def test_invalid_inputs(prices, message):
    with pytest.raises(ValueError) as error:
        checkout_total(prices)
    assert str(error.value) == message
