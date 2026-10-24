# pricing.py decisions

- Discounts compound: each known code multiplies the running total by (1 - pct/100), in list order.
- A code listed twice applies twice, matching "apply each code in order".
- Code matching is exact and case-sensitive (`save10` is unknown and ignored).
- Negative quantities count as 0 via `max(quantity, 0)`; unit prices are used as given.
- Rounding happens once, on the final total, with `round(total, 2)` per the design.
- Floats are kept per the design; `round()` on floats can land half-cent cases on either side (e.g. 2.675 -> 2.67). Decimal would be safer for payments if the design allows it.
- Empty items or no codes return 0.0 / the undiscounted total.
