# Decisions

- Implemented the design as written: float math, discounts compounded in order, one `round(total, 2)` at the end.
- Codes match exactly (case-sensitive); unknown codes are skipped.
- A repeated code is applied each time it appears, since the design says to apply each code in order.
- Negative quantities count as 0 via `max(quantity, 0)`.
- Open for the lead: float dollars plus `round()` (banker's rounding on binary floats) can be off by a cent, e.g. 2.675 rounds to 2.67. Decimal or integer cents would be safer for payments.
- Open for the lead: should duplicate codes stack, and should SAVE10 + SAVE25 combine (they compound to 32.5%)?
- Negative unit prices are not validated because the design doesn't cover them.
