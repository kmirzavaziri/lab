# checkout_total decisions
- Subtotal = sum of unit_price * max(quantity, 0); negative quantities count as 0.
- Codes apply in list order, each compounding on the running total (SAVE10 then SAVE25 = 0.9 * 0.75).
- Unknown codes are skipped; code matching is exact and case-sensitive.
- A code listed twice is applied twice, per "apply each code".
- Rounding happens once, on the final total, with round(total, 2).
- Float math per the design; round() uses banker's rounding on float values, so half-cent edges may round down. Decimal would be safer for money.
