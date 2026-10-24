# Decisions

- Money math uses `Decimal` (prices parsed via `str()`), so float error never reaches a total.
- Final rounding is `quantize(0.01, ROUND_HALF_UP)`, which differs from the design's `round()`: 2.675 -> 2.68, not 2.67.
- The return value is a float with 2 decimals, matching the design's return type.
- Discounts compound in list order: each multiplies the running total by `1 - pct/100`.
- Each code applies at most once per checkout; repeats are ignored so a code list can't stack the same discount.
- Unknown codes are ignored; matching is exact and case-sensitive.
- Negative quantities count as 0. A non-int or bool quantity raises `TypeError`.
- A non-numeric or bool price raises `TypeError`; a negative, NaN or infinite price raises `ValueError`.
