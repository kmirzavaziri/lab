# pricing.py decisions
- Followed the design as written: float math, discounts compound in order, `round(total, 2)` once at the end.
- Codes match exactly (case-sensitive); unknown codes are skipped.
- Repeated codes are applied each time they appear (the design says "apply each code"); the design does not cap stacking.
- Negative quantities count as 0 via `max(quantity, 0)`; negative prices are left as given.
- Concern for review: floats plus `round()` (banker's rounding on binary floats) can be off by a cent, e.g. 2.675 -> 2.67. A payments service should use `Decimal` with ROUND_HALF_UP; I kept floats because the design specifies them.
- Concern for review: unlimited stacking (SAVE25 x N) lets a customer drive the total toward 0; product should confirm whether to dedupe or allow one code.
