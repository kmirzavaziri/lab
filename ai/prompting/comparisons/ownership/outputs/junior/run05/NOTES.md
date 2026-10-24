# pricing.py decisions
- Implemented the design as written: float dollars, round(total, 2) once at the end.
- Discounts compound: each known code multiplies the running total by (1 - pct/100), in list order.
- Repeated codes apply each time (e.g. SAVE10 twice = 19% off); the design sets no limit.
- Unknown codes are skipped; code matching is exact and case-sensitive.
- Negative quantities count as 0; negative unit prices are not checked.
- Review flag: float money plus round() (banker's rounding on binary floats) can be off by a cent; Decimal with ROUND_HALF_UP is safer for payments.
- Review flag: stacking and repeating codes is unbounded; confirm with the tech lead whether that is intended.
