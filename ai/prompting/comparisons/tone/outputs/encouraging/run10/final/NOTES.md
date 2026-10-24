# checkout_total decisions
- Math runs in Decimal (prices via str()) so float drift cannot skew totals; the result is returned as a float.
- Final rounding uses round(total, 2) per the design; on Decimal that is round-half-even (banker's). Flag: payments often want ROUND_HALF_UP.
- Bad input fails loudly: non-numeric, bool, NaN/inf or negative unit_price, and non-int or bool quantity raise TypeError/ValueError.
- Negative quantities count as 0, per the design; malformed item tuples raise on unpacking.
- discount_codes passed as a bare string raises TypeError, so "SAVE10" is never iterated per character; non-str codes raise too.
- Codes compound in order on the running total; matching is exact and case-sensitive; unknown codes are skipped.
- Flag: a repeated code applies again (the design says apply each code), so SAVE25 twice stacks; dedupe if that is unwanted.
- The discount table is read-only (MappingProxyType) so callers cannot mutate rates at runtime.
