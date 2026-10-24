# checkout_total decisions

- Money math in `Decimal` (prices converted via `str`), so float error never reaches the total.
- Final rounding is `quantize(0.01, ROUND_HALF_UP)` instead of `round()`: `round()` is banker's rounding on floats and misrounds halves like 2.675.
- Returns a `float` so callers and tests compare against plain numbers.
- Discounts compound in the given order; each known code applies at most once per checkout (repeating SAVE10 is a stacking exploit).
- Codes match case- and whitespace-insensitively; unknown or non-string codes are ignored.
- Negative quantity counts as 0, per the design.
- Invalid input fails loudly: negative, NaN or infinite price raises `ValueError`; non-numeric price or non-int quantity (incl. bool) raises `TypeError`.
- `discount_codes=None` is treated as no codes.
