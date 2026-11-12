def checkout_total(prices: list[int]) -> int:
    if not isinstance(prices, list):
        raise ValueError("prices must be a list")
    if len(prices) < 1:
        raise ValueError("at least 1 item is required")
    if len(prices) > 100:
        raise ValueError("at most 100 items are allowed")
    total = 0
    for price in prices:
        if type(price) is not int:
            raise ValueError("price must be an integer")
        if price < 10:
            raise ValueError("price must be at least 10")
        if price > 500:
            raise ValueError("price must be at most 500")
        total += price
    return total
