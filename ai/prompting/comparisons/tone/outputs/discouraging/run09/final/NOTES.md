# checkout_total decisions
- Money math runs in Decimal (floats converted via str) so totals are exact; result is quantized once at the end.
- Rounding is ROUND_HALF_UP to cents, deviating from built-in round(): round() on floats/banker's rounding mis-rounds .xx5 (2.675 -> 2.67); return type stays float.
- Subtotal = sum(unit_price * max(quantity, 0)); negative quantities count as 0 per the design.
- Codes apply multiplicatively in list order to the running total; repeats apply each time, per "apply each code in order".
- Codes match after strip() and upper(); unknown codes, non-string codes and a None list are ignored.
- Invalid input raises instead of producing a wrong charge: non-numeric/bool/NaN/infinite/negative unit_price, non-int quantity, malformed item tuples.
- Open product question: whether stacking or repeating codes should be allowed at all; kept as specified.
