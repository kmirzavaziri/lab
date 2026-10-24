# checkout_total decisions
- Money math runs in Decimal (prices parsed via str) so float drift never reaches a charged amount; the result is a float for the existing interface.
- Final rounding is ROUND_HALF_UP to the cent, the convention for currency; built-in round() on floats rounds half-to-even and misrounds values like 2.675.
- Rounding happens once, on the final total, so stacked discounts do not compound rounding error.
- Discounts stack multiplicatively in the given order (SAVE10 + SAVE25 = 32.5% off), so the total never goes below zero.
- Each code applies at most once per checkout; repeating a code cannot stack it again.
- Codes match case- and whitespace-insensitively; unknown or non-string codes are ignored.
- Negative quantity counts as 0, per the design.
- Negative, non-finite or non-numeric prices and non-int quantities raise, since they signal a caller bug that would otherwise silently misprice an order.
