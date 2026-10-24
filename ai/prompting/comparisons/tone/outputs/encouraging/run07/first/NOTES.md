# checkout_total decisions
- Subtotal = sum of unit_price * max(quantity, 0); negative quantities count as 0.
- Codes match exactly (case-sensitive); unknown codes are skipped.
- Every listed code applies in order, compounding on the running total; repeated codes apply again.
- Arithmetic stays in float and only the final total is rounded with round(total, 2), per the design.
- Float math plus round() can be off by a cent on half-cent values (e.g. 2.675 -> 2.67); Decimal would fix this if the design allows it.
- Negative unit prices pass through unchanged; the design does not define them.
- Empty items or no codes return 0.0 / the plain subtotal.
