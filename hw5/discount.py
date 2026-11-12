def checkout_with_discount(prices: list[int], is_member: bool) -> int:
    discount_threshold = 1_000
    discount_percent = 10
    shipping_fee = 60
    subtotal = 0
    for price in prices:
        subtotal += price
    meets_threshold = subtotal >= discount_threshold
    discount = 0
    if is_member & meets_threshold:
        discount = subtotal * discount_percent // 100
    discounted_subtotal = subtotal - discount
    return discounted_subtotal + shipping_fee
