# checkout_total decisions
- Money math uses Decimal (prices via str()) so float error never reaches the total; returns a float.
- Final rounding is Decimal ROUND_HALF_UP to cents instead of round(), which rounds half-to-even and on float artifacts (round(2.675, 2) == 2.67).
- Each discount code applies at most once; repeating SAVE25 does not stack (abuse vector). Distinct codes still compound in order.
- Codes are matched after strip() + upper(); unknown or non-string codes are ignored.
- Negative quantity counts as 0, per spec.
- Negative, NaN or infinite unit prices raise ValueError; a negative price would silently lower someone else's total.
- Non-int quantities (floats, bools) raise TypeError rather than being truncated.
- discount_codes=None is treated as no codes.
