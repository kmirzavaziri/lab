# checkout_total decisions
- Money math runs in Decimal; each float price converts via str(), so 0.1 stays 0.1, not its binary approximation.
- Subtotal = sum of unit_price * max(quantity, 0); negative quantities count as 0.
- Bad input raises: TypeError for non-number prices, or non-int or bool quantities; ValueError for negative, NaN or infinite prices, or items that are not 3-tuples.
- Codes match exactly (case-sensitive) against DISCOUNT_PERCENTAGES: SAVE10=10, SAVE25=25.
- Each known code multiplies the running total by (1 - pct/100) in list order; a repeated code applies again, per the design.
- Unknown codes are skipped.
- Rounding happens once at the end with round(total, 2) on the Decimal (half-even), then returns a float.
- Empty items return 0.0.
