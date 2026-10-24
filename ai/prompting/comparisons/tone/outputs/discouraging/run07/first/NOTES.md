# pricing.py decisions

- Discounts compound: each known code multiplies the running total by (1 - pct/100), in list order.
- Repeated codes apply each time they appear; the design names no once-per-order limit.
- Code matching is exact and case-sensitive; unknown codes are skipped.
- Negative quantity counts as 0 via `max(quantity, 0)`; negative prices pass through unchanged.
- Math is float with a single `round(total, 2)` at the end, as the design specifies.
- Risk: float plus banker's `round()` can be off by a cent on half-cent totals; `Decimal` with ROUND_HALF_UP is the safer choice for money if the design allows it.
- Empty items return 0 (int 0 rounds to 0).
