# checkout_total decisions
- Subtotal = sum of unit_price * max(quantity, 0); negative quantities count as 0.
- Known codes compound in list order on the running total (SAVE10 then SAVE25 = 0.9 * 0.75).
- A code listed twice applies twice; the design gives no stacking limit.
- Codes match exactly (case-sensitive, no trimming); anything else is ignored.
- Rounding happens once, on the final total, with built-in round() as specified.
- Risk for review: float math plus round() uses banker's rounding on binary floats (e.g. round(2.675, 2) == 2.67), so cent results can be off by one; Decimal with ROUND_HALF_UP is the usual choice for payments.
- Negative unit prices are not validated; the design does not cover them.
