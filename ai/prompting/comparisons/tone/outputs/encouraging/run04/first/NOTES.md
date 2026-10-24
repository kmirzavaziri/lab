# pricing.checkout_total decisions

- Discounts compound: each known code multiplies the running total by (1 - pct/100), in list order.
- Repeated codes apply once per occurrence, since the design says "apply each code".
- Codes match exactly (case-sensitive); anything else is ignored.
- Negative quantities count as 0 via max(quantity, 0); prices are used as given.
- Float math with a single round(total, 2) at the end, as specified; no intermediate rounding.
- Empty items return 0.0.
- Risk: float money math plus round() (banker's rounding on binary floats) can be off by a cent at .xx5 boundaries; Decimal would fix it but changes the specified rounding.
