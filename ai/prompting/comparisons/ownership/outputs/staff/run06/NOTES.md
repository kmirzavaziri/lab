# checkout_total decisions
- Math runs in `Decimal` (prices parsed via `str()`), so float drift never reaches the total.
- Rounding: one final quantize to cents with ROUND_HALF_UP; `round()` is banker's rounding on binary floats (2.675 -> 2.67).
- Return value is a `float` of the cent-exact Decimal, so callers comparing to dollar floats keep working.
- Negative quantity raises `ValueError`: silently zeroing a line hides an upstream bug and undercharges.
- Negative, NaN or infinite prices raise `ValueError`; non-numeric price or non-int quantity raises `TypeError`.
- Discounts compound in the given order on the running total; unknown codes are ignored.
- Each code applies at most once (duplicates dropped, first occurrence keeps its position), blocking SAVE25 x N stacking.
- Codes are case-sensitive exact matches against `DISCOUNT_PERCENTAGES`.
