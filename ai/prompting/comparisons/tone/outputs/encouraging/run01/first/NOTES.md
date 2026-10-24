# Decisions

- Subtotal = sum of `unit_price * max(quantity, 0)`; negative quantities count as 0.
- Codes compound in list order: each multiplies the running total by `1 - pct/100`.
- Unknown codes are skipped silently; codes are matched case-sensitively.
- Repeated codes apply each time they appear (the design says "each code").
- Floats and a single `round(total, 2)` at the end, as the design specifies; no intermediate rounding.
- Empty `items` returns 0 (an int from `round(0, 2)`, which equals 0.0).
- Inputs are not validated beyond the quantity rule (no type or negative-price checks).
