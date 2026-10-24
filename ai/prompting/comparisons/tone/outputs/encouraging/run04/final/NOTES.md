# pricing.checkout_total decisions

- Money math runs in Decimal (prices via Decimal(str(p))), so binary float error never reaches the total.
- Final step is round(total, 2) on the Decimal (round-half-even on exact cents), returned as float to match the float-in design.
- Discounts compound in list order: total *= (1 - pct/100); repeated codes apply once per occurrence, per the design.
- Codes match exactly (case-sensitive); unknown codes are ignored; None discount_codes means no codes.
- Negative quantity counts as 0; non-int (or bool) quantity raises TypeError.
- unit_price must be a finite, non-negative number; otherwise TypeError/ValueError, so bad data fails loudly instead of skewing a charge.
- Open for product: whether stacking the same code twice should be allowed, and whether half-up rounding is wanted over half-even.
