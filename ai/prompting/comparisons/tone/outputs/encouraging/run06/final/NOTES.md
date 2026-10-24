# pricing.py decisions

- Money math runs in `Decimal`; each price enters as `Decimal(str(price))`, so 0.1 stays exactly 0.1 and float drift never reaches the total.
- The final total is `round(total, 2)` on the Decimal (half-even to cents), returned as a float to match the float-in-dollars interface.
- Discount codes live in `DISCOUNT_PERCENTAGES`; they compound in list order, a repeated code applies again, and matching is exact and case-sensitive.
- Unknown codes are skipped; negative quantities count as 0.
- Bad input raises before any total is returned: a non-numeric, bool, NaN, infinite or negative `unit_price`, or a non-int or bool `quantity`.
- A malformed item (not a 3-tuple) raises the natural unpacking `ValueError`/`TypeError`.
