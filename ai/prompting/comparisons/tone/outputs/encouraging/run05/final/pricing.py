from collections.abc import Iterable
from decimal import Decimal
from numbers import Real

DISCOUNT_PERCENTAGES: dict[str, Decimal] = {
    "SAVE10": Decimal(10),
    "SAVE25": Decimal(25),
}


def _to_price(unit_price: object) -> Decimal:
    if isinstance(unit_price, bool) or not isinstance(unit_price, Real):
        raise TypeError(f"unit_price must be a number, got {type(unit_price).__name__}")
    price = Decimal(str(unit_price))
    if not price.is_finite():
        raise ValueError(f"unit_price must be finite, got {unit_price}")
    if price < 0:
        raise ValueError(f"unit_price must not be negative, got {unit_price}")
    return price


def _to_quantity(quantity: object) -> int:
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError(f"quantity must be an int, got {type(quantity).__name__}")
    return max(quantity, 0)


def checkout_total(
    items: Iterable[tuple[str, float, int]],
    discount_codes: Iterable[str],
) -> float:
    total = Decimal(0)
    for _name, unit_price, quantity in items:
        total += _to_price(unit_price) * _to_quantity(quantity)
    for code in discount_codes:
        if not isinstance(code, str):
            raise TypeError(f"discount code must be a str, got {type(code).__name__}")
        percentage = DISCOUNT_PERCENTAGES.get(code)
        if percentage is None:
            continue
        total -= total * percentage / 100
    return float(round(total, 2))
