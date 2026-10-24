from decimal import ROUND_HALF_UP, Decimal

DISCOUNT_PERCENTAGES = {
    "SAVE10": Decimal("10"),
    "SAVE25": Decimal("25"),
}

CENT = Decimal("0.01")


def _to_decimal(value):
    if isinstance(value, bool) or not isinstance(value, (int, float, Decimal, str)):
        raise TypeError(f"unsupported price type: {type(value).__name__}")
    amount = Decimal(str(value))
    if not amount.is_finite():
        raise ValueError(f"price must be finite: {value!r}")
    return amount


def checkout_total(items, discount_codes):
    total = Decimal("0")
    for name, unit_price, quantity in items:
        price = _to_decimal(unit_price)
        if price < 0:
            raise ValueError(f"negative unit price for {name!r}: {unit_price!r}")
        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise TypeError(f"quantity for {name!r} must be an int: {quantity!r}")
        total += price * max(quantity, 0)

    applied = set()
    for code in discount_codes or ():
        if not isinstance(code, str):
            continue
        normalized = code.strip().upper()
        percentage = DISCOUNT_PERCENTAGES.get(normalized)
        if percentage is None or normalized in applied:
            continue
        applied.add(normalized)
        total -= total * percentage / Decimal("100")

    return float(total.quantize(CENT, rounding=ROUND_HALF_UP))
