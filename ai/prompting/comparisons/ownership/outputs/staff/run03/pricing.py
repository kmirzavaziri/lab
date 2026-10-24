from decimal import ROUND_HALF_UP, Decimal

DISCOUNT_PERCENTAGES = {
    "SAVE10": Decimal("10"),
    "SAVE25": Decimal("25"),
}

CENT = Decimal("0.01")


def _to_decimal(value):
    if isinstance(value, bool) or not isinstance(value, (int, float, Decimal, str)):
        raise TypeError(f"unit_price must be numeric, got {type(value).__name__}")
    amount = Decimal(str(value))
    if not amount.is_finite():
        raise ValueError(f"unit_price must be finite, got {value}")
    return amount


def checkout_total(items, discount_codes):
    subtotal = Decimal("0")
    for name, unit_price, quantity in items:
        price = _to_decimal(unit_price)
        if price < 0:
            raise ValueError(f"negative unit_price for {name!r}: {unit_price}")
        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise TypeError(f"quantity for {name!r} must be int, got {type(quantity).__name__}")
        if quantity < 0:
            raise ValueError(f"negative quantity for {name!r}: {quantity}")
        subtotal += price * quantity

    unknown = [code for code in discount_codes if code not in DISCOUNT_PERCENTAGES]
    if unknown:
        raise ValueError(f"unknown discount codes: {unknown}")

    total = subtotal
    for code in dict.fromkeys(discount_codes):
        total -= total * DISCOUNT_PERCENTAGES[code] / 100

    return float(total.quantize(CENT, rounding=ROUND_HALF_UP))
