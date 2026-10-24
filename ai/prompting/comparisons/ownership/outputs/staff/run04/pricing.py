from decimal import ROUND_HALF_UP, Decimal

DISCOUNT_PERCENTAGES = {
    "SAVE10": Decimal("10"),
    "SAVE25": Decimal("25"),
}

CENT = Decimal("0.01")


def _to_decimal(value):
    if isinstance(value, bool) or not isinstance(value, (int, float, str, Decimal)):
        raise TypeError(f"unit_price must be numeric, got {type(value).__name__}")
    amount = Decimal(str(value))
    if not amount.is_finite():
        raise ValueError(f"unit_price must be finite, got {value!r}")
    if amount < 0:
        raise ValueError(f"unit_price must be non-negative, got {value!r}")
    return amount


def _to_quantity(value):
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"quantity must be an int, got {type(value).__name__}")
    return max(value, 0)


def checkout_total(items, discount_codes):
    total = Decimal("0")
    for _name, unit_price, quantity in items:
        total += _to_decimal(unit_price) * _to_quantity(quantity)

    applied = set()
    for code in discount_codes or ():
        if not isinstance(code, str):
            continue
        key = code.strip().upper()
        percentage = DISCOUNT_PERCENTAGES.get(key)
        if percentage is None or key in applied:
            continue
        applied.add(key)
        total -= total * percentage / Decimal("100")

    return float(total.quantize(CENT, rounding=ROUND_HALF_UP))
