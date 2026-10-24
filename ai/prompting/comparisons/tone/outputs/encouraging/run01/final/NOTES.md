# Decisions

- Math runs in `Decimal` (prices parsed via `str`) so float binary error never reaches the total.
- Final rounding is `quantize(0.01, ROUND_HALF_UP)` in place of `round()`: `round()` on floats gives 2.675 -> 2.67; half-up gives 2.68.
- Returns a `float` so callers and tests keep the float interface; full precision until the final rounding.
- Negative quantity counts as 0; prices must be finite, non-negative real numbers, and quantities ints (bools rejected) — otherwise `TypeError`/`ValueError`.
- Codes compound in list order (`total *= 1 - pct/100`); repeated codes apply each time; matching is case-sensitive.
- Unknown codes are skipped silently, per the design.
- Empty `items` returns `0.0`.
