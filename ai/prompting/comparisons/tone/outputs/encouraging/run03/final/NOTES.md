# Decisions

- Math runs in Decimal (prices via str() so 0.1 stays 0.1); the result is quantized to cents with ROUND_HALF_UP and returned as a float.
- This replaces the design's float `round()`, which uses banker's rounding on binary floats and can be a cent off (e.g. 2.675 -> 2.67).
- Discounts compound in list order; a repeated code applies again, per "apply each code in order".
- Codes match exactly (case-sensitive); unknown codes are skipped, per the design.
- Negative quantities clamp to 0, per the design.
- Bad input fails loudly: non-numeric, bool, NaN/inf or negative unit_price, and non-int or bool quantity raise TypeError/ValueError.
- Open for product: should duplicate codes stack, and should codes be case-insensitive?
