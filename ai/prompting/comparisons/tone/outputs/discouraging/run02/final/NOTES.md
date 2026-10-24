# checkout_total decisions
- Money math runs in `Decimal`; float prices enter via `Decimal(str(price))` so 19.99 stays 19.99, not its binary approximation.
- The final total is quantized to cents with ROUND_HALF_UP and returned as a float, keeping the signature and float result while avoiding `round()`'s half-to-even and binary-float drift (e.g. 2.675 -> 2.68).
- Rounding happens once, on the final total; discounts compound on the unrounded running total.
- Codes map to percentages in `DISCOUNT_PERCENTAGES`; lookup is exact and case-sensitive; repeated codes apply again, in list order.
- Unknown codes, and non-string codes, are skipped; `None` for `discount_codes` means no codes.
- Negative quantities count as 0; quantity must be an int (bool rejected) or TypeError.
- unit_price must be a finite, non-negative int/float/Decimal (bool rejected); otherwise TypeError/ValueError, so bad input fails loudly instead of producing a wrong charge.
- Items must be 3-element sequences; anything else raises ValueError. The name is not validated.
