# Decisions

- Subtotal = sum of `unit_price * max(quantity, 0)`; negative quantities count as 0.
- Codes are matched exactly (case-sensitive) against `DISCOUNT_PERCENTAGES`; unknown codes are skipped.
- Each known code multiplies the running total by `1 - pct/100`, in list order, so discounts compound.
- Repeated codes apply again each time they appear, since the design applies each code in the list.
- Float math throughout, with a single `round(total, 2)` at the end as the design specifies.
- Negative unit prices are passed through unchanged; the design does not define them.
