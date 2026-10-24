# pricing.py decisions
- Implemented the design as written: float math, `round(total, 2)` applied once at the end.
- Negative quantities clamp to 0 via `max(quantity, 0)`.
- Unknown codes are skipped silently; known codes compound in list order on the running total.
- Duplicate codes are not deduplicated (SAVE10 twice applies 10% twice), since the design says "apply each code".
- Codes match exactly (case-sensitive, no whitespace trimming).
- Raised for review: floats plus `round()` (banker's rounding on binary floats) can be off by a cent; Decimal with ROUND_HALF_UP is the usual choice for payments.
- Raised for review: stacking codes is unbounded; the design does not cap or forbid it.
- No input validation (negative prices, non-numeric values) since the design specifies none.
