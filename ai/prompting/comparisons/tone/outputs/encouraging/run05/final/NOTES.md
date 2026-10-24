# Decisions

- Math runs in `Decimal` (prices via `str`) for exact cents; `round(total, 2)` on the Decimal (half-even), returned as float.
- Discounts compound on the running total in list order; duplicate codes apply per occurrence (design is literal; confirm).
- Unknown codes are skipped; matching is case-sensitive (`save10` is unknown).
- Negative quantities count as 0, per design.
- Invalid input raises instead of producing a wrong charge: non-numeric, bool, NaN/inf or negative price; non-int or bool quantity; non-str code.
- Malformed item tuples raise the natural unpacking `ValueError`.
- Empty `items` returns 0.0. Float return keeps the design's contract; returning `Decimal` would be safer for callers.
