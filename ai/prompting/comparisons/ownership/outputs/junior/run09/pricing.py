DISCOUNT_PERCENTAGES = {
    "SAVE10": 10,
    "SAVE25": 25,
}


def checkout_total(items, discount_codes):
    total = 0.0
    for _name, unit_price, quantity in items:
        total += unit_price * max(quantity, 0)

    for code in discount_codes:
        percentage = DISCOUNT_PERCENTAGES.get(code)
        if percentage is None:
            continue
        total *= 1 - percentage / 100

    return round(total, 2)
