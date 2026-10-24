import math
from decimal import ROUND_HALF_UP, Decimal

DISCOUNT_PERCENTAGES = {
    "SAVE10": Decimal(10),
    "SAVE25": Decimal(25),
}

CENT = Decimal("0.01")
HUNDRED = Decimal(100)


def _line_total(item):
    name, unit_price, quantity = item
    if isinstance(unit_price, bool) or not isinstance(unit_price, (int, float)):
        raise TypeError(f"unit_price for {name!r} must be a number")
    if not math.isfinite(unit_price) or unit_price < 0:
        raise ValueError(f"unit_price for {name!r} must be a finite, non-negative number")
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError(f"quantity for {name!r} must be an int")
    return Decimal(str(unit_price)) * max(quantity, 0)


def checkout_total(items, discount_codes):
    total = sum((_line_total(item) for item in items), Decimal(0))
    for code in discount_codes:
        percentage = DISCOUNT_PERCENTAGES.get(code) if isinstance(code, str) else None
        if percentage is None:
            continue
        total *= 1 - percentage / HUNDRED
    return float(total.quantize(CENT, rounding=ROUND_HALF_UP))
