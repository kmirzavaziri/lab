# checkout_total decisions
- Codes map to percentages in `DISCOUNT_PERCENTAGES`; lookup is exact and case-sensitive.
- Each code is applied multiplicatively to the running total, in list order; repeated codes apply again.
- Unknown codes are skipped; negative quantities count as 0 via `max(quantity, 0)`.
- Rounding happens once, on the final total, with built-in `round(total, 2)` as specified.
- Float math and `round()` (banker's rounding on binary floats) follow the design; for live money, Decimal with ROUND_HALF_UP would avoid cent drift.
- Negative unit prices and non-int quantities pass through unvalidated, as the design is silent on them.
