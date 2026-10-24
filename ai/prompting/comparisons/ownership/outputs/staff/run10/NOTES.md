# checkout_total decisions

- Math runs in `Decimal` (prices converted via `str`), so float drift never reaches money.
- Final rounding is half-up to cents via `quantize`; `round()` on floats rounds half-to-even on binary values (e.g. 2.675 -> 2.67).
- Returns a `float` to keep the signature tests expect; rounding happens once, at the end.
- Each code applies at most once: a repeated SAVE25 stacking to 43.75% off is a revenue leak.
- Codes are matched after `strip().upper()`; unknown or non-string codes are ignored.
- Negative quantity counts as 0, per spec; non-int (or bool) quantity raises `TypeError`.
- Negative, NaN or infinite unit price raises `ValueError`: bad catalog data must fail loudly, never discount the cart.
- `discount_codes=None` is treated as no codes.
