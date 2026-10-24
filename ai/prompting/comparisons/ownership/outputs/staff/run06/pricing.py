from decimal import ROUND_HALF_UP, Decimal

DISCOUNT_PERCENTAGES = {
    "SAVE10": Decimal("10"),
    "SAVE25": Decimal("25"),
}

CENT = Decimal("0.01")


def _to_money(value):
    if isinstance(value, bool) or not isinstance(value, (int, float, Decimal, str)):
        raise TypeError(f"unit_price must be numeric, got {type(value).__name__}")
    amount = Decimal(str(value))
    if not amount.is_finite():
        raise ValueError(f"unit_price must be finite, got {value!r}")
    if amount < 0:
        raise ValueError(f"unit_price must not be negative, got {value!r}")
    return amount


def _to_quantity(value):
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"quantity must be an int, got {type(value).__name__}")
    if value < 0:
        raise ValueError(f"quantity must not be negative, got {value!r}")
    return value


def checkout_total(items, discount_codes):
    total = Decimal("0")
    for name, unit_price, quantity in items:
        total += _to_money(unit_price) * _to_quantity(quantity)

    for code in dict.fromkeys(discount_codes):
        percentage = DISCOUNT_PERCENTAGES.get(code)
        if percentage is not None:
            total -= total * percentage / 100

    return float(total.quantize(CENT, rounding=ROUND_HALF_UP))
