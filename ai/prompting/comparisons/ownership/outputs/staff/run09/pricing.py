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
        raise ValueError(f"unit_price must be non-negative, got {value!r}")
    return amount


def _to_quantity(value):
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"quantity must be an int, got {type(value).__name__}")
    if value < 0:
        raise ValueError(f"quantity must be non-negative, got {value}")
    return value


def checkout_total(items, discount_codes):
    subtotal = Decimal("0")
    for name, unit_price, quantity in items:
        subtotal += _to_money(unit_price) * _to_quantity(quantity)

    applied = set()
    total = subtotal
    for code in discount_codes or ():
        normalized = code.strip().upper() if isinstance(code, str) else None
        percentage = DISCOUNT_PERCENTAGES.get(normalized)
        if percentage is None or normalized in applied:
            continue
        applied.add(normalized)
        total -= total * percentage / Decimal("100")

    return float(total.quantize(CENT, rounding=ROUND_HALF_UP))
