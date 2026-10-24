# checkout_total decisions
- Money math runs in Decimal; each float price converts via str(), so 0.1 stays 0.1 exactly.
- Final total rounds once with round(total, 2) under ROUND_HALF_UP (2.675 -> 2.68) and returns a float.
- Subtotal = sum of unit_price * max(quantity, 0); negative quantities count as 0.
- Codes match exactly (case-sensitive); unknown codes are skipped; each listed code compounds in order, repeats included.
- Raises TypeError for a non-numeric price or non-int quantity (bool rejected for both).
- Raises ValueError for a negative, NaN or infinite unit price.
- Empty items return 0.0.
