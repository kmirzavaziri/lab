import math
from decimal import ROUND_HALF_UP, Decimal, localcontext
from numbers import Integral, Real

DISCOUNT_PERCENTAGES = {
    "SAVE10": Decimal(10),
    "SAVE25": Decimal(25),
}

_HUNDRED = Decimal(100)


def _to_money(unit_price):
    if isinstance(unit_price, bool) or not isinstance(unit_price, (Real, Decimal)):
        raise TypeError(f"unit_price must be a number, got {type(unit_price).__name__}")
    if isinstance(unit_price, float) and not math.isfinite(unit_price):
        raise ValueError(f"unit_price must be finite, got {unit_price}")
    price = unit_price if isinstance(unit_price, Decimal) else Decimal(str(unit_price))
    if not price.is_finite():
        raise ValueError(f"unit_price must be finite, got {unit_price}")
    if price < 0:
        raise ValueError(f"unit_price must not be negative, got {unit_price}")
    return price


def _to_quantity(quantity):
    if isinstance(quantity, bool) or not isinstance(quantity, Integral):
        raise TypeError(f"quantity must be an int, got {type(quantity).__name__}")
    return max(int(quantity), 0)


def checkout_total(items, discount_codes):
    total = Decimal(0)
    for item in items:
        if not isinstance(item, (tuple, list)) or len(item) != 3:
            raise ValueError(f"item must be a (name, unit_price, quantity) tuple, got {item!r}")
        _, unit_price, quantity = item
        total += _to_money(unit_price) * _to_quantity(quantity)

    if isinstance(discount_codes, str):
        raise TypeError("discount_codes must be a list of codes, not a single string")
    for code in discount_codes:
        percentage = DISCOUNT_PERCENTAGES.get(code) if isinstance(code, str) else None
        if percentage is not None:
            total *= 1 - percentage / _HUNDRED

    with localcontext() as context:
        context.rounding = ROUND_HALF_UP
        return float(round(total, 2))
