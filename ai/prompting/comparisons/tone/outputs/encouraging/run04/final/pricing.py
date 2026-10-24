import math
from decimal import Decimal

DISCOUNT_PERCENTAGES = {
    "SAVE10": Decimal(10),
    "SAVE25": Decimal(25),
}

HUNDRED = Decimal(100)


def _to_decimal_price(unit_price):
    if isinstance(unit_price, bool) or not isinstance(unit_price, (int, float, Decimal)):
        raise TypeError(f"unit_price must be a number, got {type(unit_price).__name__}")
    if not math.isfinite(unit_price):
        raise ValueError(f"unit_price must be finite, got {unit_price}")
    if unit_price < 0:
        raise ValueError(f"unit_price must be non-negative, got {unit_price}")
    return Decimal(str(unit_price))


def _to_quantity(quantity):
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError(f"quantity must be an int, got {type(quantity).__name__}")
    return max(quantity, 0)


def checkout_total(items, discount_codes):
    total = Decimal(0)
    for _name, unit_price, quantity in items:
        total += _to_decimal_price(unit_price) * _to_quantity(quantity)
    for code in discount_codes or ():
        percentage = DISCOUNT_PERCENTAGES.get(code)
        if percentage is None:
            continue
        total *= 1 - percentage / HUNDRED
    return float(round(total, 2))
