# Decisions
- Codes are compounded in list order on the running total (SAVE10 then SAVE25 = 32.5% off).
- Repeated codes apply each time they appear; the design sets no stacking limit.
- Code matching is exact and case-sensitive; unknown codes are skipped.
- Negative quantities count as 0 via max(quantity, 0); negative prices pass through as given.
- Floats and round(total, 2) follow the design; rounding happens once, on the final total.
- Empty items or no codes return 0.0 or the undiscounted total.
