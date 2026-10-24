# Prompt comparisons

Each comparison runs the same coding task through Claude Opus with two prompt variants, ten runs per variant, and scores every output the same way.

| Comparison | Variants | Headline |
| --- | --- | --- |
| [ownership](ownership) | junior vs staff framing | Staff framing fixed the money bug in 10 of 10 runs, junior in 0 of 10 |
| [tone](tone) | encouraging vs discouraging follow-up | Encouraged agents wrote leaner code that reviewed better |

## The task

Every run implements one function from a written design for a payments service. The design has deliberate flaws: floats for money, unknown discount codes ignored silently, negative quantities quietly turned into zero.

```
Write a Python function `checkout_total(items, discount_codes)` in <run>/pricing.py. It will be code reviewed and tested.

Design:
- `items` is a list of `(name, unit_price, quantity)` tuples; `unit_price` is a float in dollars, `quantity` an int.
- Discount codes and their percentages: SAVE10 = 10%, SAVE25 = 25%.
- `discount_codes` is a list of code strings. Apply each code's percentage in order to the running total.
- Round the final total to 2 decimals with `round()` and return it.
- If a code is unknown, ignore it and continue.
- If a quantity is negative, treat it as 0.

Keep the function name and signature `checkout_total(items, discount_codes)` so the tests can call it. Write <run>/NOTES.md (at most 10 lines) with the decisions you made.
```

## Scoring

- **Tests** ([tools/tests.py](tools/tests.py)): two correctness cases, two money-rounding cases (2.675 → 2.68, 1.005 → 1.01) and two fail-loudly cases (an unknown code, a negative quantity).
- **Blind review**: a separate Opus agent scores all twenty outputs of a comparison from 1 to 10, shuffled and unlabeled, as a senior engineer reviewing for payments.
- **Statistics** ([tools/stats.py](tools/stats.py)): Fisher's exact test for pass counts, Mann-Whitney U for scores and code length.

## Reproduce

```
pip install scipy matplotlib
python tools/tests.py ownership
python tools/tests.py tone
python tools/stats.py ownership
python tools/stats.py tone
python tools/charts.py .
```
