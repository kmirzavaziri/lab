from decimal import ROUND_HALF_UP, Decimal
from math import isfinite
from typing import Iterable, Sequence

CENT = Decimal("0.01")

DISCOUNT_PERCENTAGES = {
    "SAVE10": Decimal(10),
    "SAVE25": Decimal(25),
}


def _to_decimal_price(unit_price) -> Decimal:
    if isinstance(unit_price, bool) or not isinstance(unit_price, (int, float, Decimal)):
        raise TypeError(f"unit_price must be a number, got {type(unit_price).__name__}")
    if isinstance(unit_price, float) and not isfinite(unit_price):
        raise ValueError(f"unit_price must be finite, got {unit_price}")
    price = Decimal(str(unit_price)) if isinstance(unit_price, float) else Decimal(unit_price)
    if not price.is_finite():
        raise ValueError(f"unit_price must be finite, got {unit_price}")
    if price < 0:
        raise ValueError(f"unit_price must not be negative, got {unit_price}")
    return price


def _to_quantity(quantity) -> int:
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError(f"quantity must be an int, got {type(quantity).__name__}")
    return max(quantity, 0)


def checkout_total(
    items: Iterable[Sequence],
    discount_codes: Iterable[str],
) -> float:
    total = Decimal(0)
    for item in items:
        if len(item) != 3:
            raise ValueError(f"item must be (name, unit_price, quantity), got {item!r}")
        _name, unit_price, quantity = item
        total += _to_decimal_price(unit_price) * _to_quantity(quantity)
    for code in discount_codes or ():
        percentage = DISCOUNT_PERCENTAGES.get(code) if isinstance(code, str) else None
        if percentage is None:
            continue
        total *= (Decimal(100) - percentage) / Decimal(100)
    return float(total.quantize(CENT, rounding=ROUND_HALF_UP))
