# pricing.py decisions

- Money math runs in `Decimal`; floats convert via `str()`, so 2.675 stays 2.675 instead of 2.67499...
- Final total uses `round(total, 2)` under ROUND_HALF_UP (checkout convention) and returns a `float` per the design.
- Discounts compound in list order on the unrounded running total; repeated codes apply each time, as the design says.
- Unknown or non-string codes are skipped; codes match exactly (case-sensitive).
- Negative quantities count as 0; bool, float or non-int quantities raise `TypeError`.
- Prices must be finite, non-negative numbers (bool rejected); otherwise `TypeError`/`ValueError`.
- Malformed items (not a 3-tuple) raise `ValueError`; a bare string for `discount_codes` raises `TypeError`.
- Open question for the product owner: should a code stack when repeated (SAVE10 twice = 19% off)?
