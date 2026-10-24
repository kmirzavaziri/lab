# checkout_total decisions

- Math in `Decimal` (prices via `str()`), so float drift never reaches the charged amount.
- Final rounding is half-up to cents via `quantize`, not `round()`: `round()` is banker's rounding on a binary float (`round(2.675, 2) == 2.67`). Returns `float` to keep the signature's contract.
- Negative quantity raises `ValueError` instead of becoming 0: silently zeroing it hides an upstream cart bug and undercharges. Negative, NaN or infinite prices raise too; non-int quantities and non-numeric prices raise `TypeError`.
- Unknown codes are ignored, as designed: a mistyped promo code should not fail the checkout.
- Codes are trimmed and upper-cased; each code applies at most once, so repeating `SAVE25` cannot stack it.
- Discounts compound on the running total in order (10% then 25% = 32.5% off); since they multiply, order does not change the result.
- Discount table is a module constant `DISCOUNT_PERCENTAGES`; `discount_codes=None` is treated as no codes.
