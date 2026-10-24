# Decisions

- Followed the design as written: float dollars, `round(total, 2)` only on the final total.
- Codes stack multiplicatively in list order (SAVE10 then SAVE25 = 0.9 * 0.75 of the subtotal).
- Repeated codes apply each time they appear; the design names no limit.
- Unknown codes are skipped; code matching is exact and case-sensitive.
- Negative quantities count as 0 via `max(quantity, 0)`; unit prices are taken as given.
- For review: float math plus `round()` (banker's rounding on exact ties) can be off by a cent; `Decimal` with ROUND_HALF_UP is the usual choice for payments. I kept floats because the design specifies them.
