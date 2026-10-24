# pricing.py decisions

- All math runs in `Decimal`; prices enter via `Decimal(str(price))`, so 0.1 stays exactly 0.10.
- Discounts compound in list order on the unrounded running total; repeated codes apply each time, as the design states.
- One `round(total, 2)` at the end, on the Decimal (half-even, per the design's `round()`); the result returns as a float.
- Unknown codes are skipped; matching is exact and case-sensitive.
- Negative quantity counts as 0.
- Invalid input raises: non-numeric, NaN, infinite or negative price -> TypeError/ValueError; non-int or bool quantity -> TypeError; non-str code -> TypeError; a malformed item tuple -> ValueError.
- Empty items return 0.0.
