# Decisions

- Implemented the design as written: float math, `round(total, 2)` only on the final total.
- Discounts compound: each known code multiplies the running total by `(1 - pct/100)`, in list order.
- Repeated codes are applied each time they appear, since the design says "apply each code".
- Codes match exactly and are case-sensitive (`save10` counts as unknown and is skipped).
- Negative quantities count as 0, and an empty cart returns 0.0.
- Unit prices are not validated, so a negative price lowers the total.
- For the tech lead: float dollars plus `round()` (banker's rounding) can drift by a cent; payments usually use `Decimal` with ROUND_HALF_UP. I kept floats as the design says.
- Also for the tech lead: unlimited stacking (for example SAVE25 x N) may need a cap.
