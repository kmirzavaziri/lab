import importlib.util
import json
import sys
from decimal import Decimal
from pathlib import Path

CASES = [
    ("correct", "basic total", ([("a", 19.99, 3)], []), "59.97"),
    ("correct", "stacked codes", ([("a", 100.0, 1)], ["SAVE10", "SAVE25"]), "67.50"),
    ("money", "half-up 2.675", ([("a", 2.675, 1)], []), "2.68"),
    ("money", "half-up 1.005", ([("a", 1.005, 1)], []), "1.01"),
    ("loud", "unknown code", ([("a", 10.0, 1)], ["SAVEALL"]), "raise"),
    ("loud", "negative quantity", ([("a", 10.0, -2)], []), "raise"),
]


def load(path):
    spec = importlib.util.spec_from_file_location("pricing_under_test", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.checkout_total


def run_case(checkout_total, args, expected):
    try:
        result = checkout_total(*args)
    except Exception as error:
        return expected == "raise", f"raised {type(error).__name__}"
    if expected == "raise":
        return False, f"returned {result!r}"
    return Decimal(str(result)) == Decimal(expected), f"returned {result!r}"


def main(experiment):
    outputs = Path(experiment) / "outputs"
    report = {}
    for path in sorted(outputs.rglob("pricing.py")):
        checkout_total = load(path)
        report[str(path.parent.relative_to(outputs))] = [
            {"group": group, "case": name, "passed": passed, "detail": detail}
            for group, name, args, expected in CASES
            for passed, detail in [run_case(checkout_total, args, expected)]
        ]
    (Path(experiment) / "results" / "tests.json").write_text(json.dumps(report, indent=1) + "\n")


main(sys.argv[1])
