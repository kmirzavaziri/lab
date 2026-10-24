from decimal import ROUND_HALF_UP, Decimal
from numbers import Real

DISCOUNT_PERCENTAGES = {
    "SAVE10": Decimal("10"),
    "SAVE25": Decimal("25"),
}

CENT = Decimal("0.01")
HUNDRED = Decimal("100")


def _to_decimal_price(unit_price):
    if isinstance(unit_price, bool) or not isinstance(unit_price, Real):
        raise TypeError(f"unit_price must be a number, got {type(unit_price).__name__}")
    price = Decimal(str(unit_price))
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
    for _, unit_price, quantity in items:
        total += _to_decimal_price(unit_price) * _to_quantity(quantity)

    applied = set()
    for code in discount_codes:
        percentage = DISCOUNT_PERCENTAGES.get(code)
        if percentage is None or code in applied:
            continue
        applied.add(code)
        total *= 1 - percentage / HUNDRED

    return float(total.quantize(CENT, rounding=ROUND_HALF_UP))
