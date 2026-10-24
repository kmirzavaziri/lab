from decimal import ROUND_HALF_UP, Context, Decimal, localcontext
from numbers import Integral, Real

DISCOUNT_PERCENTAGES = {
    "SAVE10": Decimal("10"),
    "SAVE25": Decimal("25"),
}

CENT = Decimal("0.01")
HUNDRED = Decimal("100")
_CONTEXT = Context(prec=34, rounding=ROUND_HALF_UP)


def _to_price(unit_price, name):
    if isinstance(unit_price, bool) or not isinstance(unit_price, Real):
        raise TypeError(f"unit_price for {name!r} must be a real number")
    price = Decimal(str(unit_price))
    if not price.is_finite():
        raise ValueError(f"unit_price for {name!r} must be finite")
    if price < 0:
        raise ValueError(f"unit_price for {name!r} must not be negative")
    return price


def _to_quantity(quantity, name):
    if isinstance(quantity, bool) or not isinstance(quantity, Integral):
        raise TypeError(f"quantity for {name!r} must be an int")
    return max(int(quantity), 0)


def checkout_total(items, discount_codes):
    with localcontext(_CONTEXT):
        total = Decimal(0)
        for item in items:
            name, unit_price, quantity = item
            total += _to_price(unit_price, name) * _to_quantity(quantity, name)

        for code in discount_codes:
            percentage = DISCOUNT_PERCENTAGES.get(code) if isinstance(code, str) else None
            if percentage is None:
                continue
            total *= (HUNDRED - percentage) / HUNDRED

        return float(total.quantize(CENT, rounding=ROUND_HALF_UP))
