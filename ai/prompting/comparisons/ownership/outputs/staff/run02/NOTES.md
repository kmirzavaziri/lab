# pricing.checkout_total decisions

- Money math in `Decimal` (prices parsed via `str()`), so float drift never reaches the total.
- Final rounding is `quantize(0.01, ROUND_HALF_UP)` instead of `round()`: `round()` on floats is banker's rounding on binary values (`round(2.675, 2) == 2.67`), wrong for money.
- No intermediate rounding; only the final total is rounded. Returns a `float` to keep the call contract.
- Discounts compound in the given order, as designed (SAVE10 then SAVE25 = 32.5% off).
- Each code applies at most once per checkout; repeating SAVE25 would otherwise stack toward 100% off.
- Unknown codes are ignored; matching is exact and case-sensitive.
- Negative quantity counts as 0, as designed. Non-int (or bool) quantity raises `TypeError`.
- Negative, NaN or infinite `unit_price` raises `ValueError`: bad price data must fail loudly, never lower a charge.
