# Decisions

- Math runs in `Decimal`; each price converts via `str()`, so 0.1 means exactly 0.1. The return value is a float, matching the design.
- Spec deviation: the final rounding is ROUND_HALF_UP to cents, where the design said `round()`. Python's `round()` uses banker's rounding on floats and gets half-cents wrong (`round(2.675, 2)` gives 2.67, half-up gives 2.68).
- Negative quantities count as 0, per the design.
- Bad input raises: a non-number, NaN, infinite or negative price, or a non-int quantity (bools rejected), with the item name in the error.
- Codes match exactly and are case-sensitive. Unknown or non-string codes are ignored.
- Codes stack multiplicatively in list order, and a repeated code applies each time it appears. A cap on stacking is a product decision left open.
- An empty cart returns 0.0.
