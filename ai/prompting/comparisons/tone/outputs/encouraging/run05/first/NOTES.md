# Decisions

- Arithmetic runs in `Decimal` (prices converted via `str`) to avoid float drift; the result is a float rounded with `round(..., 2)`.
- Rounding happens once, on the final total, as the design specifies.
- Discounts compound: each known code takes its percentage off the running total, in list order.
- Duplicate codes apply once per occurrence, per "apply each code in order"; worth confirming this is intended.
- Unknown codes are skipped; codes match case-sensitively (`save10` is unknown).
- Negative quantities count as 0 via `max(quantity, 0)`.
- Empty `items` returns 0.0.
