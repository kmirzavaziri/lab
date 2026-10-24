# pricing.py decisions
- Discounts compound: each known code multiplies the running total by (1 - pct/100), in list order.
- Duplicate codes apply once per occurrence, since the design says "apply each code".
- Code matching is exact and case-sensitive; anything not SAVE10/SAVE25 is skipped.
- Negative quantity contributes 0 via max(quantity, 0); unit_price is used as given.
- Float math throughout, with a single round(total, 2) at the end, as the design specifies.
- Empty items or no codes return 0.0 / the undiscounted subtotal.
