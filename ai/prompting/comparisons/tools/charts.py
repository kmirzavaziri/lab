import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_SECONDARY = "#52514e"
GRID = "#e4e3df"
BLUE = "#2a78d6"
ORANGE = "#eb6834"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 13,
    "axes.edgecolor": GRID,
    "axes.labelcolor": INK_SECONDARY,
    "xtick.color": INK_SECONDARY,
    "ytick.color": INK_SECONDARY,
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
})


def style(ax):
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.tick_params(length=0)
    ax.grid(axis="x", color=GRID, linewidth=1)
    ax.set_axisbelow(True)


def count_panel(ax, title, values, labels, colors, total, p_value):
    rows = range(len(values))
    ax.barh(list(rows), values, color=colors, height=0.55, edgecolor=SURFACE, linewidth=2)
    for row, value in zip(rows, values):
        ax.text(value + total * 0.02, row, f"{value} of {total}", va="center", color=INK, fontsize=13)
    ax.set_yticks(list(rows), labels, color=INK, fontsize=13)
    ax.set_xlim(0, total * 1.25)
    ax.set_xticks([0, total // 2, total])
    ax.invert_yaxis()
    ax.set_title(title, loc="left", color=INK, fontsize=14, fontweight="bold")
    ax.text(0, -0.22, p_value, transform=ax.transAxes, va="bottom", ha="left", color=INK_SECONDARY, fontsize=11)
    style(ax)


def strip_panel(ax, title, groups, labels, colors, p_value, x_range, x_label):
    for row, (values, color) in enumerate(zip(groups, colors)):
        counts = {value: values.count(value) for value in values}
        seen = {}
        offsets = []
        for value in values:
            index = seen.get(value, 0)
            seen[value] = index + 1
            offsets.append(row + (index - (counts[value] - 1) / 2) * 0.1)
        ax.scatter(values, offsets, s=90, color=color, edgecolor=SURFACE, linewidth=2, zorder=3)
        mean = sum(values) / len(values)
        ax.plot([mean, mean], [row - 0.3, row + 0.3], color=INK, linewidth=2, zorder=4)
        ax.text(mean, row - 0.38, f"avg {mean:.1f}", ha="center", va="bottom", color=INK, fontsize=12)
    ax.set_yticks(range(len(groups)), labels, color=INK, fontsize=13)
    ax.set_xlim(*x_range)
    ax.set_ylim(len(groups) - 0.4, -0.75)
    ax.set_xlabel(x_label)
    ax.set_title(title, loc="left", color=INK, fontsize=14, fontweight="bold")
    ax.text(0, -0.22, p_value, transform=ax.transAxes, va="bottom", ha="left", color=INK_SECONDARY, fontsize=11)
    style(ax)


def figure(headline, note, panels, path):
    fig, axes = plt.subplots(1, len(panels), figsize=(16, 7.2), gridspec_kw={"wspace": 0.45})
    for ax, draw in zip(axes, panels):
        draw(ax)
    fig.suptitle(headline, x=0.06, y=0.98, ha="left", color=INK, fontsize=20, fontweight="bold")
    fig.text(0.06, 0.02, note, ha="left", color=INK_SECONDARY, fontsize=11)
    fig.subplots_adjust(left=0.1, right=0.97, top=0.8, bottom=0.2)
    fig.savefig(path, dpi=110)
    plt.close(fig)


def tests_for(experiment):
    return json.loads((experiment / "results" / "tests.json").read_text())


def scores_for(experiment):
    return json.loads((experiment / "results" / "review-scores.json").read_text())


def money(cases):
    return cases[2]["passed"] and cases[3]["passed"]


def loud(cases):
    return cases[4]["passed"] or cases[5]["passed"]


def main(root):
    root = Path(root)
    runs = [f"run{index:02d}" for index in range(1, 11)]

    ownership = root / "ownership"
    tests = tests_for(ownership)
    scores = scores_for(ownership)
    junior = [f"junior/{run}" for run in runs]
    staff = [f"staff/{run}" for run in runs]
    figure(
        "Same model, same task: the staff prompt fixed the money bug every time",
        "Claude Opus, 10 runs per prompt, one checkout task with a flawed design. Counts: Fisher's exact test. Scores: Mann-Whitney U, blind reviewer.",
        [
            lambda ax: count_panel(ax, "Fixed money rounding", [sum(money(tests[run]) for run in junior), sum(money(tests[run]) for run in staff)], ["Junior", "Staff"], [BLUE, ORANGE], 10, "p < 0.0001"),
            lambda ax: count_panel(ax, "Made bad input fail loudly", [sum(loud(tests[run]) for run in junior), sum(loud(tests[run]) for run in staff)], ["Junior", "Staff"], [BLUE, ORANGE], 10, "p = 0.21, not significant"),
            lambda ax: strip_panel(ax, "Blind review score", [[scores[run] for run in junior], [scores[run] for run in staff]], ["Junior", "Staff"], [BLUE, ORANGE], "p = 0.0002", (1, 10.5), "score out of 10"),
        ],
        ownership / "ownership-results.png",
    )

    tone = root / "tone"
    tests = tests_for(tone)
    scores = scores_for(tone)
    encouraging = [f"encouraging/{run}" for run in runs]
    discouraging = [f"discouraging/{run}" for run in runs]
    lengths = {run: sum(1 for _ in open(tone / "outputs" / run / "final" / "pricing.py")) for run in encouraging + discouraging}
    figure(
        "Encouraged agents wrote leaner code that reviewed better",
        "Claude Opus, 10 runs per tone. Same first prompt, then one follow-up that differs only in tone. Counts: Fisher's exact test. Others: Mann-Whitney U.",
        [
            lambda ax: count_panel(ax, "Fixed money rounding", [sum(money(tests[run + "/final"]) for run in encouraging), sum(money(tests[run + "/final"]) for run in discouraging)], ["Encouraging", "Discouraging"], [BLUE, ORANGE], 10, "p = 0.66, not significant"),
            lambda ax: strip_panel(ax, "Length of final code", [[lengths[run] for run in encouraging], [lengths[run] for run in discouraging]], ["Encouraging", "Discouraging"], [BLUE, ORANGE], "p = 0.03", (25, 55), "lines"),
            lambda ax: strip_panel(ax, "Blind review score", [[scores[run] for run in encouraging], [scores[run] for run in discouraging]], ["Encouraging", "Discouraging"], [BLUE, ORANGE], "p = 0.017", (1, 10.5), "score out of 10"),
        ],
        tone / "tone-results.png",
    )


main(sys.argv[1])
