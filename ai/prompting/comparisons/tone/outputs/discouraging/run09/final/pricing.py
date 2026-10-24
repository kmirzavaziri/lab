from decimal import ROUND_HALF_UP, Decimal

DISCOUNT_PERCENTAGES = {
    "SAVE10": Decimal("10"),
    "SAVE25": Decimal("25"),
}

CENT = Decimal("0.01")
HUNDRED = Decimal("100")


def _to_money(value, field):
    if isinstance(value, bool) or not isinstance(value, (int, float, Decimal)):
        raise TypeError(f"{field} must be a number, got {type(value).__name__}")
    amount = Decimal(str(value)) if isinstance(value, float) else Decimal(value)
    if not amount.is_finite():
        raise ValueError(f"{field} must be finite, got {value!r}")
    if amount < 0:
        raise ValueError(f"{field} must not be negative, got {value!r}")
    return amount


def _to_quantity(value):
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"quantity must be an int, got {type(value).__name__}")
    return max(value, 0)


def checkout_total(items, discount_codes):
    total = Decimal("0")
    for item in items:
        if len(item) != 3:
            raise ValueError(f"item must be (name, unit_price, quantity), got {item!r}")
        _name, unit_price, quantity = item
        total += _to_money(unit_price, "unit_price") * _to_quantity(quantity)
    for code in discount_codes or ():
        if not isinstance(code, str):
            continue
        percentage = DISCOUNT_PERCENTAGES.get(code.strip().upper())
        if percentage is None:
            continue
        total = total * (HUNDRED - percentage) / HUNDRED
    return float(total.quantize(CENT, rounding=ROUND_HALF_UP))
