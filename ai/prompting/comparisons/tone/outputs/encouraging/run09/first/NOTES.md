# Decisions

- Codes live in a module-level `DISCOUNT_PERCENTAGES` map; unknown codes are skipped.
- Discounts compound in list order: each multiplies the running total by `1 - pct/100`.
- Repeated codes apply each time they appear; the design sets no limit.
- Negative quantities are clamped to 0 with `max(quantity, 0)`.
- Arithmetic is float, rounded once at the end with `round(total, 2)`, as the design says.
- `round()` uses banker's rounding on float values, so half-cent totals can round down (e.g. 2.675 -> 2.67).
- Empty `items` returns 0.0, or 0 for an int sum; codes do not change a zero total.
