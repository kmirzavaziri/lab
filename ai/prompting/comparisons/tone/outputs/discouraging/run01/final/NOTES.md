# pricing.py decisions
- Money math runs in Decimal; float prices enter via Decimal(str(price)) so 0.1 stays 0.1, no binary drift.
- Final step is round(total, 2) on the Decimal (exact half-even), returned as float to match the float-dollar input.
- Discounts compound in list order: each known code multiplies the running total by (1 - pct/100); duplicates apply per occurrence.
- Codes match exactly (case-sensitive); unknown codes are skipped and logged at INFO.
- Negative quantity counts as 0, per the design.
- Rejected with TypeError: non-numeric or bool price, non-int or bool quantity, non-str code.
- Rejected with ValueError: negative, NaN or infinite price; malformed item tuples raise on unpacking.
- Empty items return 0.0.
