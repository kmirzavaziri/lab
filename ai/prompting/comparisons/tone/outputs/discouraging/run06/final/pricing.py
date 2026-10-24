import math
from decimal import Decimal
from numbers import Real

DISCOUNT_PERCENTAGES = {"SAVE10": Decimal(10), "SAVE25": Decimal(25)}


def _to_money(unit_price):
    if isinstance(unit_price, bool) or not isinstance(unit_price, Real):
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
    for item in items:
        if len(item) != 3:
            raise ValueError(f"item must be (name, unit_price, quantity), got {item!r}")
        _, unit_price, quantity = item
        total += _to_money(unit_price) * _to_quantity(quantity)
    for code in discount_codes:
        if not isinstance(code, str):
            raise TypeError(f"discount code must be a str, got {type(code).__name__}")
        percentage = DISCOUNT_PERCENTAGES.get(code)
        if percentage is not None:
            total *= 1 - percentage / 100
    return float(round(total, 2))
