# pricing.py decisions

- Money math runs in `Decimal` (prices via `str()` so 0.1 stays 0.1) in a local context, so global decimal state is untouched.
- Rounding is once, at the end, to cents with ROUND_HALF_UP; `round()` on floats is banker's rounding over binary values (2.675 -> 2.67), wrong for payments. Result is returned as a float to keep the interface.
- Discounts compound in list order: each known code multiplies the running total by (100 - pct)/100; a repeated code applies again, per "apply each code in order".
- Codes match exactly and case-sensitively; unknown or non-string codes are ignored.
- Negative quantity counts as 0; bool or non-integer quantity raises TypeError.
- unit_price must be a finite, non-negative real number (not bool), else TypeError/ValueError; a malformed item tuple raises ValueError on unpacking.
- Invalid input fails loudly instead of producing a wrong charge.
