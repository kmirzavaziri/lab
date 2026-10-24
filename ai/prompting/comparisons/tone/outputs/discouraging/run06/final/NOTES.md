# Decisions
- Money math uses Decimal; each float price converts via str() so 0.1 means exactly 0.10, with no float drift across items.
- Codes compound in list order on the running total (SAVE10 then SAVE25 = 32.5% off); repeats apply each time, as the design sets no stacking limit.
- Codes match exactly (case-sensitive); unknown codes are skipped; a non-str code raises TypeError.
- Negative quantity counts as 0; a non-int or bool quantity raises TypeError.
- unit_price must be a finite, non-negative real number (bool rejected); otherwise TypeError/ValueError, so bad data never yields a silent wrong charge.
- An item that is not a 3-tuple raises ValueError.
- Rounding happens once, on the final total, with round(total, 2) per the design; on Decimal this rounds half-even (0.125 -> 0.12).
- Open question for owners: payments usually want ROUND_HALF_UP; switching is one line if the design allows it.
- Returns float to match the design; empty cart returns 0.0.
