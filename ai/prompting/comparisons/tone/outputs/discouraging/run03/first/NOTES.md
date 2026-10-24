# pricing.py decisions

- Followed the design literally: float arithmetic, `round(total, 2)` only on the final total.
- Discounts compound in list order on the running total (SAVE10 then SAVE25 = 0.9 * 0.75).
- Repeated codes apply each time they appear; the design gives no single-use rule.
- Codes match exactly (case-sensitive); unknown codes are skipped.
- Negative quantities count as 0 via `max(quantity, 0)`; negative prices are left as given.
- Empty `items` returns 0 (an int from `round(0, 2)`), which compares equal to 0.0.
- Risk: floats plus `round()` can misround half-cents (e.g. 2.675 -> 2.67); Decimal would fix it but changes the design.
