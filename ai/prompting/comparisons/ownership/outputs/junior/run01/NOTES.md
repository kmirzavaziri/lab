# pricing.py decisions
- Implemented as designed: float math, codes compound in order on the running total, `round(total, 2)` at the end.
- Unknown codes are skipped; negative quantities count as 0 via `max(quantity, 0)`.
- Repeated codes apply again each time (design says "apply each code"); flag for the lead if stacking should be capped.
- Risk to raise in review: floats plus `round()` can be off by a cent (e.g. 2.675 -> 2.67, banker's rounding on ties).
  For a payments service I would propose `Decimal` with `ROUND_HALF_UP`, but kept the design's float/round as specified.
- Code matching is exact and case-sensitive ("save10" is unknown); empty items return 0.0.
