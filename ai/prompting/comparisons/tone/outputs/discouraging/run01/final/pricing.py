import logging
import math
from decimal import Decimal
from numbers import Real

logger = logging.getLogger(__name__)

DISCOUNT_PERCENTAGES = {
    "SAVE10": Decimal("10"),
    "SAVE25": Decimal("25"),
}

HUNDRED = Decimal("100")


def _to_decimal_price(name, unit_price):
    if isinstance(unit_price, bool) or not isinstance(unit_price, Real):
        raise TypeError(f"unit_price for {name!r} must be a number, got {type(unit_price).__name__}")
    if not math.isfinite(unit_price):
        raise ValueError(f"unit_price for {name!r} must be finite, got {unit_price!r}")
    if unit_price < 0:
        raise ValueError(f"unit_price for {name!r} must not be negative, got {unit_price!r}")
    return Decimal(str(unit_price))


def _to_quantity(name, quantity):
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError(f"quantity for {name!r} must be an int, got {type(quantity).__name__}")
    return max(quantity, 0)


def checkout_total(items, discount_codes):
    total = Decimal("0")
    for item in items:
        name, unit_price, quantity = item
        total += _to_decimal_price(name, unit_price) * _to_quantity(name, quantity)

    for code in discount_codes:
        if not isinstance(code, str):
            raise TypeError(f"discount code must be a str, got {type(code).__name__}")
        percentage = DISCOUNT_PERCENTAGES.get(code)
        if percentage is None:
            logger.info("Ignoring unknown discount code %r", code)
            continue
        total *= 1 - percentage / HUNDRED

    return float(round(total, 2))
