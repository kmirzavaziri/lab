from decimal import ROUND_HALF_UP, Decimal

DISCOUNT_PERCENTAGES = {
    "SAVE10": Decimal("10"),
    "SAVE25": Decimal("25"),
}

CENT = Decimal("0.01")


def checkout_total(items, discount_codes):
    total = Decimal("0")
    for name, unit_price, quantity in items:
        price = Decimal(str(unit_price))
        if not price.is_finite() or price < 0:
            raise ValueError(f"invalid unit_price for {name!r}: {unit_price!r}")
        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise TypeError(f"quantity for {name!r} must be an int: {quantity!r}")
        total += price * max(quantity, 0)

    applied = set()
    for code in discount_codes:
        percentage = DISCOUNT_PERCENTAGES.get(code)
        if percentage is None or code in applied:
            continue
        applied.add(code)
        total -= total * percentage / 100

    return float(total.quantize(CENT, rounding=ROUND_HALF_UP))
