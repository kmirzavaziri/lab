# pricing.py decisions

- Discount codes live in a module-level `DISCOUNT_PERCENTAGES` dict, so adding a code is one line.
- Codes compound in list order: each multiplies the running total by `1 - pct/100`.
- A code listed twice applies twice, since the design says "apply each code".
- Code matching is exact and case-sensitive (`save10` counts as unknown and is skipped).
- Negative quantities are clamped to 0 with `max(quantity, 0)`.
- Arithmetic is float as specified; only the final total is rounded with `round(total, 2)`, never intermediate values.
- Inputs are not validated beyond the design (for example, negative prices pass through unchanged).
