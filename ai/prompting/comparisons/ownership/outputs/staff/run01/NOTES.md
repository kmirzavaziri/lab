# checkout_total decisions

- Money math runs in `Decimal` (prices via `str()`), so float drift never reaches the total.
- Final rounding is half-up to cents via `quantize`; `round()` on floats is banker's rounding on binary values (e.g. 2.675 -> 2.67).
- Returns a `float` rounded to 2 decimals, matching the signature callers expect.
- Discounts compound in order on the unrounded running total; rounding happens once at the end.
- Each code applies at most once: repeating SAVE10 does not stack.
- Codes match case-insensitively after trimming whitespace; unknown or non-string codes are ignored.
- Negative quantity counts as 0; a non-int (or bool) quantity raises `TypeError`.
- Negative, NaN or infinite unit prices raise `ValueError`; non-numeric prices raise `TypeError`.
- `discount_codes=None` is treated as no codes.
