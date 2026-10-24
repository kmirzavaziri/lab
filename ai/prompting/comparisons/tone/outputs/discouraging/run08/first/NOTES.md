# checkout_total decisions
- Subtotal = sum of unit_price * max(quantity, 0); negative quantities count as 0.
- Codes are looked up exactly (case-sensitive) in a module-level table: SAVE10=10, SAVE25=25.
- Each known code multiplies the running total by (1 - pct/100), in list order.
- Repeated codes are applied each time they appear, per "apply each code in order".
- Unknown codes are skipped silently.
- Rounding happens once, at the end, with round(total, 2), so no intermediate rounding.
- Float math is kept as the design specifies; round() uses banker's rounding on exact halves.
- Empty items or empty codes give 0.0 / the undiscounted subtotal.
