# checkout_total decisions

- Money math runs in `Decimal` (prices converted via `str()`), so float drift never reaches a charged amount.
- Final rounding is half-up to cents via `quantize`; `round()` uses banker's rounding on inexact floats (2.675 -> 2.67).
- Return value stays a `float` so the existing signature and callers keep working.
- Negative quantity raises `ValueError`: coercing to 0 hides upstream cart bugs and silently drops line items from a charge.
- Negative or non-finite unit price raises `ValueError`; non-int (or bool) quantity raises `TypeError`.
- Unknown discount code raises `ValueError` before any math: silently ignoring it charges the customer full price for a typo.
- Each code applies once per checkout (duplicates dropped), so repeating SAVE25 cannot stack the discount.
- Discounts compound on the running total in the given order, matching the design.
