import json
import sys
from pathlib import Path

from scipy.stats import fisher_exact, mannwhitneyu

EXPERIMENTS = {
    "ownership": {"variants": ("junior", "staff"), "suffix": ""},
    "tone": {"variants": ("encouraging", "discouraging"), "suffix": "/final"},
}
RUNS = [f"run{index:02d}" for index in range(1, 11)]


def p_value_text(p_value):
    return "< 0.0001" if p_value < 0.0001 else f"{p_value:.4f}"


def fixed_money(cases):
    return cases[2]["passed"] and cases[3]["passed"]


def failed_loudly(cases):
    return cases[4]["passed"] or cases[5]["passed"]


def summarize(experiment):
    experiment = Path(experiment)
    config = EXPERIMENTS[experiment.name]
    tests = json.loads((experiment / "results" / "tests.json").read_text())
    scores = json.loads((experiment / "results" / "review-scores.json").read_text())
    first, second = config["variants"]

    def runs_of(variant):
        return [f"{variant}/{run}" for run in RUNS]

    def code_lines(run):
        return sum(1 for _ in open(experiment / "outputs" / (run + config["suffix"]) / "pricing.py"))

    rows = [f"| Measure | {first} | {second} | p |", "| --- | --- | --- | --- |"]
    for label, check in (("Fixed money rounding", fixed_money), ("Failed loudly on bad input", failed_loudly)):
        first_count = sum(check(tests[run + config["suffix"]]) for run in runs_of(first))
        second_count = sum(check(tests[run + config["suffix"]]) for run in runs_of(second))
        p_value = fisher_exact([[first_count, 10 - first_count], [second_count, 10 - second_count]])[1]
        rows.append(f"| {label} | {first_count}/10 | {second_count}/10 | {p_value_text(p_value)} (Fisher's exact) |")
    for label, measure in (("Blind review score", scores.get), ("Lines of final code", code_lines)):
        first_values = [measure(run) for run in runs_of(first)]
        second_values = [measure(run) for run in runs_of(second)]
        p_value = mannwhitneyu(first_values, second_values, alternative="two-sided").pvalue
        rows.append(f"| {label}, average | {sum(first_values) / 10:.1f} | {sum(second_values) / 10:.1f} | {p_value_text(p_value)} (Mann-Whitney U) |")
    (experiment / "results" / "stats.md").write_text("\n".join(rows) + "\n")


summarize(sys.argv[1])
