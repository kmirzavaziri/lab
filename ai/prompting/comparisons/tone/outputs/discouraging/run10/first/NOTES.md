# Decisions

- Discount table is a module-level dict `DISCOUNT_PERCENTAGES` so new codes are one-line additions.
- Codes match exactly (case-sensitive); anything not in the table is skipped.
- Repeated codes apply each time they appear, compounding on the running total, as "apply each code in order" reads.
- Negative quantities are clamped to 0 via `max(quantity, 0)`.
- Totals use float math with a single `round(total, 2)` at the end, per the design; no intermediate rounding.
- Empty `items` returns 0; no input validation beyond the design.
