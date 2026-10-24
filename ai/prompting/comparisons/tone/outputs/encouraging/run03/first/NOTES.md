# Decisions

- Discounts compound: each known code multiplies the running total by (1 - pct/100), in list order.
- Repeated codes apply each time they appear, per "apply each code in order".
- Code matching is exact and case-sensitive; anything else counts as unknown and is skipped.
- Negative quantities clamp to 0 via max(quantity, 0).
- Float math throughout, rounded once at the end with round(total, 2), as the design specifies.
- Empty items returns 0.0.
- Floats plus round() can be a cent off on half-cent totals; Decimal would fix that, but the design asks for floats and round().
