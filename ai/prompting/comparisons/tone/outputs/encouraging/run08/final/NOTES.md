# checkout_total decisions
- Money math runs in Decimal; float prices convert via str() so 0.1 stays 0.1, and the result returns as a float.
- Final total rounds once to cents with ROUND_HALF_UP; round() on floats rounds half cents to even or down (2.675 -> 2.67), which undercharges.
- Subtotal = sum of unit_price * max(quantity, 0); negative quantities count as 0.
- Codes apply in list order, compounding on the running total (SAVE10 then SAVE25 = 0.9 * 0.75).
- Unknown codes are skipped; matching is exact and case-sensitive.
- A code listed twice applies twice, per "apply each code"; worth a product decision on stacking limits.
- Bad input raises: non-numeric, NaN/inf or negative price -> TypeError/ValueError; non-int or bool quantity -> TypeError.
