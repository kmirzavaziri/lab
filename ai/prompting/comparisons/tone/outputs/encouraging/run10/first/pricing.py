from decimal import Decimal

DISCOUNT_PERCENTAGES = {
    "SAVE10": Decimal(10),
    "SAVE25": Decimal(25),
}


def checkout_total(items, discount_codes):
    total = Decimal(0)
    for _name, unit_price, quantity in items:
        total += Decimal(str(unit_price)) * max(quantity, 0)
    for code in discount_codes:
        percentage = DISCOUNT_PERCENTAGES.get(code)
        if percentage is not None:
            total -= total * percentage / 100
    return float(round(total, 2))
