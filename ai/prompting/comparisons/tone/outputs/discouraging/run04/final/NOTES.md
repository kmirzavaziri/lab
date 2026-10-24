# Decisions

- Money math runs in `Decimal`; float prices enter via `Decimal(str(price))` so 0.1 stays 0.1, and the result returns as a float.
- Final rounding is the design's `round(total, 2)`, applied once to the exact Decimal (half-even, no float drift).
- Negative quantities count as 0; non-int or bool quantities raise `TypeError`.
- Prices must be finite, non-negative numbers (int, float or Decimal); anything else raises.
- Malformed items (not a 3-tuple) raise `ValueError`; non-string codes raise `TypeError`.
- Codes match exactly (case-sensitive); unknown codes are skipped.
- Each known code multiplies the running total by `1 - pct/100` in list order, so discounts compound and repeats apply again.
- The discount table is a read-only mapping so callers cannot change rates at runtime.
