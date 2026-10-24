# Decisions

- Followed the design as written: float math, discounts applied in order to the running total, `round(total, 2)` at the end only.
- Negative quantity is clamped with `max(quantity, 0)`; unknown codes are skipped.
- Codes match exactly (case-sensitive); repeated codes apply each time they appear, since the design says "apply each code".
- Discount table lives in a module-level `DISCOUNT_PERCENTAGES` dict so new codes are one-line additions.
- Empty `items` returns `0.0`.
- Open question for the lead: floats and `round()` (banker's rounding on binary floats) can be off by a cent for money; `Decimal` with `ROUND_HALF_UP` would be exact. Kept floats per the design.
- Open question: negative `unit_price` and stacking limits (e.g. SAVE25 twice) are not validated; the design says nothing about them.
