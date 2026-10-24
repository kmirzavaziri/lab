# pricing.py decisions

- Implemented the design as written: float math, discounts compounded in list order, `round(total, 2)` only at the end.
- Negative quantity is clamped to 0 with `max(quantity, 0)`; unknown codes are skipped.
- Duplicate codes apply again (SAVE10 twice = two 10% cuts), because the design says "apply each code". Worth confirming.
- Codes match exactly (case-sensitive, no trimming), since the design doesn't mention normalization.
- No validation of negative prices or wrong types; the design doesn't cover them.
- Raise in review: float dollars plus `round()` (banker's rounding on float noise, e.g. 2.675 -> 2.67) is risky in payments. Decimal or integer cents with ROUND_HALF_UP would be safer.
