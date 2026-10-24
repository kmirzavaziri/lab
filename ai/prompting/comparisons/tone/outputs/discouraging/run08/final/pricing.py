from decimal import Decimal
from numbers import Integral, Real

DISCOUNT_PERCENTAGES = {
    "SAVE10": Decimal("10"),
    "SAVE25": Decimal("25"),
}

_HUNDRED = Decimal("100")


def _to_decimal_price(unit_price):
    if isinstance(unit_price, bool) or not isinstance(unit_price, Real):
        raise TypeError(f"unit_price must be a number, got {type(unit_price).__name__}")
    price = Decimal(str(unit_price))
    if not price.is_finite():
        raise ValueError(f"unit_price must be finite, got {unit_price!r}")
    if price < 0:
        raise ValueError(f"unit_price must not be negative, got {unit_price!r}")
    return price


def _to_quantity(quantity):
    if isinstance(quantity, bool) or not isinstance(quantity, Integral):
        raise TypeError(f"quantity must be an int, got {type(quantity).__name__}")
    return max(int(quantity), 0)


def checkout_total(items, discount_codes):
    total = Decimal("0")
    for item in items:
        _, unit_price, quantity = item
        total += _to_decimal_price(unit_price) * _to_quantity(quantity)
    for code in discount_codes:
        percentage = DISCOUNT_PERCENTAGES.get(code)
        if percentage is None:
            continue
        total *= 1 - percentage / _HUNDRED
    return float(round(total, 2))
