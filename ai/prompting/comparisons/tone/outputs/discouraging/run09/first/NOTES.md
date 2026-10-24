# checkout_total decisions
- Subtotal = sum(unit_price * max(quantity, 0)); negative quantities count as 0.
- Codes apply multiplicatively in list order to the running total (SAVE10 then SAVE25 = 0.9 * 0.75).
- Repeated codes are applied each time they appear, per "apply each code in order".
- Code lookup is exact and case-sensitive; anything not in DISCOUNT_PERCENTAGES is skipped.
- Floats and round(total, 2) only at the end, as the design specifies; no intermediate rounding.
- Known float caveat: round() on binary floats can land a cent off on .xx5 values (e.g. 2.675 -> 2.67); Decimal would fix this but changes the specified rounding.
- Unit prices are not validated; negative prices pass through as given.
