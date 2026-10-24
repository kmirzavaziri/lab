# checkout_total decisions
- Math runs in Decimal (prices via str()) so float drift cannot flip the final rounding; returns a float.
- Final rounding uses round(total, 2), which on Decimal is round-half-even, matching Python's round() semantics.
- Codes compound in order on the running total; a repeated code applies again.
- Code matching is exact and case-sensitive; unknown codes are skipped.
- Negative quantities count as 0 via max(quantity, 0).
- Empty items return 0.0; negative unit prices pass through unvalidated, as the design is silent on them.
