# Decisions

- Money math runs in `Decimal`; each float price enters via `Decimal(str(price))`, so 0.1 stays exactly 0.1 and no float drift builds up across items or discounts.
- The total is rounded once at the end with `round(total, 2)` (on a Decimal that is half-even, i.e. banker's rounding) and returned as a `float` to match the design's float-in, float-out contract.
- Discounts live in the module-level `DISCOUNT_PERCENTAGES` table; codes match case-sensitively, unknown ones are skipped, repeats compound in list order.
- Negative quantity counts as 0. A non-int or bool quantity raises `TypeError`.
- `unit_price` must be a finite, non-negative real number (not a bool); otherwise `TypeError`/`ValueError`, so bad data fails loudly instead of producing a wrong charge.
- Item `name` is not checked; an empty cart returns 0.0.
