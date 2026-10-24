from decimal import ROUND_HALF_UP, Decimal

DISCOUNT_PERCENTAGES = {
    "SAVE10": Decimal("10"),
    "SAVE25": Decimal("25"),
}

CENT = Decimal("0.01")
HUNDRED = Decimal("100")


def _to_decimal(unit_price):
    if isinstance(unit_price, bool) or not isinstance(unit_price, (int, float, Decimal)):
        raise TypeError(f"unit_price must be a number, got {type(unit_price).__name__}")
    price = Decimal(str(unit_price))
    if not price.is_finite() or price < 0:
        raise ValueError(f"unit_price must be a finite non-negative number, got {unit_price!r}")
    return price


def _to_quantity(quantity):
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError(f"quantity must be an int, got {type(quantity).__name__}")
    return max(quantity, 0)


def checkout_total(items, discount_codes):
    subtotal = Decimal("0")
    for _name, unit_price, quantity in items:
        subtotal += _to_decimal(unit_price) * _to_quantity(quantity)

    applied = set()
    for code in discount_codes or ():
        if not isinstance(code, str):
            continue
        normalized = code.strip().upper()
        percentage = DISCOUNT_PERCENTAGES.get(normalized)
        if percentage is None or normalized in applied:
            continue
        applied.add(normalized)
        subtotal -= subtotal * percentage / HUNDRED

    return float(subtotal.quantize(CENT, rounding=ROUND_HALF_UP))
