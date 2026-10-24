DISCOUNT_PERCENTAGES = {
    "SAVE10": 10,
    "SAVE25": 25,
}


def checkout_total(items, discount_codes):
    total = sum(unit_price * max(quantity, 0) for _, unit_price, quantity in items)
    for code in discount_codes:
        percentage = DISCOUNT_PERCENTAGES.get(code)
        if percentage is not None:
            total *= 1 - percentage / 100
    return round(total, 2)
