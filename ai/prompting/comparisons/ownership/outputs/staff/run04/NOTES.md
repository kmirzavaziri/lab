# checkout_total decisions

- Money math runs in `Decimal` (prices converted via `str()`), so float drift never reaches the total.
- Final rounding is half-up to cents via `Decimal.quantize`, replacing `round()`, which uses banker's rounding on binary floats (`round(2.675, 2) == 2.67`). Returns a `float` to keep the signature's contract.
- Discounts compound in the given order on the running total, as designed.
- Each code applies at most once: repeating `SAVE25` does not stack.
- Codes match case-insensitively after trimming whitespace; unknown or non-string codes are ignored.
- Negative quantity counts as 0, as designed; non-int quantity raises `TypeError`.
- Negative, NaN or infinite unit prices raise `ValueError`: a bad price is a catalog bug and must not silently lower a charge.
- `discount_codes=None` is treated as no codes.
