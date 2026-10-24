import math
from decimal import Decimal
from types import MappingProxyType

DISCOUNT_PERCENTAGES = MappingProxyType({
    "SAVE10": Decimal("10"),
    "SAVE25": Decimal("25"),
})

_HUNDRED = Decimal("100")


def _to_price(unit_price):
    if isinstance(unit_price, bool) or not isinstance(unit_price, (int, float, Decimal)):
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
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError(f"quantity must be an int, got {type(quantity).__name__}")
    return max(quantity, 0)


def checkout_total(items, discount_codes):
    total = Decimal("0")
    for item in items:
        try:
            _name, unit_price, quantity = item
        except (TypeError, ValueError) as exc:
            raise ValueError(f"item must be a (name, unit_price, quantity) tuple, got {item!r}") from exc
        total += _to_price(unit_price) * _to_quantity(quantity)

    for code in discount_codes:
        if not isinstance(code, str):
            raise TypeError(f"discount code must be a str, got {type(code).__name__}")
        percentage = DISCOUNT_PERCENTAGES.get(code)
        if percentage is None:
            continue
        total *= 1 - percentage / _HUNDRED

    return float(round(total, 2))
