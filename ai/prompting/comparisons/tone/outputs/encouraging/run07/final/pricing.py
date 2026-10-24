import math
from decimal import ROUND_HALF_UP, Decimal, localcontext

DISCOUNT_PERCENTAGES = {
    "SAVE10": Decimal(10),
    "SAVE25": Decimal(25),
}

HUNDRED = Decimal(100)


def _to_price(unit_price):
    if isinstance(unit_price, bool) or not isinstance(unit_price, (int, float)):
        raise TypeError(f"unit_price must be a number, got {type(unit_price).__name__}")
    if not math.isfinite(unit_price):
        raise ValueError(f"unit_price must be finite, got {unit_price}")
    if unit_price < 0:
        raise ValueError(f"unit_price must not be negative, got {unit_price}")
    return Decimal(str(unit_price))


def _to_quantity(quantity):
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError(f"quantity must be an int, got {type(quantity).__name__}")
    return max(quantity, 0)


def checkout_total(items, discount_codes):
    total = Decimal(0)
    for _, unit_price, quantity in items:
        total += _to_price(unit_price) * _to_quantity(quantity)
    for code in discount_codes:
        percentage = DISCOUNT_PERCENTAGES.get(code)
        if percentage is None:
            continue
        total *= 1 - percentage / HUNDRED
    with localcontext() as context:
        context.rounding = ROUND_HALF_UP
        return float(round(total, 2))
