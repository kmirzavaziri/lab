# Decisions

- Arithmetic is float, as the design specifies; only the final total is rounded, with `round(total, 2)`.
- Negative quantities count as 0 through `max(quantity, 0)`.
- Codes match exactly, so case matters and whitespace is kept: `save10` is unknown and ignored.
- Codes stack multiplicatively in list order, and a repeated code applies again each time it appears.
- An empty cart, or one where every quantity is negative, returns 0.
- Open risk: float math with Python's banker's rounding can be off by a cent on half-cent totals; switch to `Decimal` with ROUND_HALF_UP if exact cents matter.
