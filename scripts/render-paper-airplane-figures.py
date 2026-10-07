"""Render SVG figures: python3 scripts/render-paper-airplane-figures.py.

Requires Matplotlib. Committed SVGs need no Python at Slidev runtime.
Conditions, dimensions and distances are fictional example settings.
Distances are means of five trials per aircraft. Geometry is schematic.
"""
from pathlib import Path
import csv
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Polygon, PathPatch
from matplotlib.path import Path as PlotPath

ROOT = Path(__file__).resolve().parents[1]
MEDIA = ROOT / 'public' / 'media'
for weight in ('Regular', 'Bold'):
    font_manager.fontManager.addfont(ROOT / 'public' / 'fonts' / f'BIZUDPGothic-{weight}.ttf')
plt.rcParams.update({
    'font.family': ['DejaVu Sans', 'BIZ UDPGothic'],
    'font.size': 22,
    'svg.fonttype': 'path',
    'svg.hashsalt': 'paper-airplane-example',
})
BLUE = '#002060'
GRAY = '#555555'
BODY_LENGTH_CM = 18
with (MEDIA / 'flight-distance.csv').open(newline='') as source:
    rows = list(csv.DictReader(source))
wing_spans = {row['condition']: int(row['wing_span_cm']) for row in rows}


def save(fig, filename):
    fig.savefig(MEDIA / filename, format='svg', facecolor='white', metadata={'Date': None})
    plt.close(fig)


def diagram(width=540, height=400):
    fig = plt.figure(figsize=(width / 100, height / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set(xlim=(0, width), ylim=(height, 0))
    ax.axis('off')
    return fig, ax


def plane(ax, x, width, top=85, bottom=285):
    fold = bottom - 32
    for side, fill in [(-1, '#ffffff'), (1, '#eef0f3')]:
        ax.add_patch(Polygon([(x, top), (x + side * width, bottom), (x, fold)],
                             facecolor=fill, edgecolor='#4b5560', linewidth=1.6, joinstyle='round'))
    ax.plot([x, x], [top, bottom - 9], color='#4b5560', linewidth=1.6)


# Three wing spans with dimension arrows; common body length is 18 cm.
fig, ax = diagram(height=430)
scale = 240 / BODY_LENGTH_CM
for x, condition in zip([85, 265, 445], 'ABC'):
    span = wing_spans[condition]
    width = span * scale / 2
    ax.text(x, 24, condition, ha='center', va='center', fontsize=25, weight='bold')
    plane(ax, x, width, top=65, bottom=305)
    for edge in [x - width, x + width]:
        ax.plot([edge, edge], [311, 348], color='#888888', linewidth=1)
    ax.annotate('', xy=(x - width, 339), xytext=(x + width, 339),
                arrowprops={'arrowstyle': '<->', 'color': BLUE, 'lw': 1.5,
                            'shrinkA': 0, 'shrinkB': 0})
    ax.text(x, 391, f'{span} cm', ha='center', va='center', fontsize=26)
save(fig, 'paper-airplanes.svg')

# Horizontal distance from release position to first contact with the floor.
fig, ax = diagram(height=420)
ax.plot([25, 515], [300, 300], color=GRAY, linewidth=1.8)
ax.text(508, 284, '床', ha='right', fontsize=22, color=GRAY)
ax.plot([85, 85], [148, 351], color='#888888', linestyle=(0, (4, 4)), linewidth=1.4)
ax.plot([455, 455], [300, 351], color='#888888', linestyle=(0, (4, 4)), linewidth=1.4)
trajectory = PlotPath([(98, 154), (270, 84), (365, 175), (455, 300)],
                      [PlotPath.MOVETO, PlotPath.CURVE4, PlotPath.CURVE4, PlotPath.CURVE4])
ax.add_patch(PathPatch(trajectory, facecolor='none', edgecolor=BLUE, linewidth=2, linestyle=(0, (5, 4))))
ax.add_patch(Polygon([(66, 134), (134, 142), (80, 164), (86, 147)],
                     facecolor='#dedede', edgecolor=BLUE, linewidth=1.7))
ax.plot(455, 300, 'o', markersize=7, color=BLUE)
ax.text(91, 93, '投げる位置', ha='center', fontsize=22)
ax.text(394, 64, '最初に床に\n触れた位置', ha='center', va='top', fontsize=22, linespacing=1.4)
ax.annotate('', xy=(451, 287), xytext=(414, 156),
            arrowprops={'arrowstyle': '-', 'color': GRAY, 'lw': 1.2})
ax.annotate('', xy=(85, 344), xytext=(455, 344),
            arrowprops={'arrowstyle': '<->', 'color': BLUE, 'lw': 2, 'shrinkA': 0, 'shrinkB': 0})
ax.text(270, 394, '水平距離', ha='center', fontsize=24, color=BLUE, weight='bold')
save(fig, 'flight-measurement.svg')

# The two levels of averaging are distinct from individual trial measurements.
fig, ax = diagram()
for y, label in [(50, '5試行の飛距離'), (187, '機体ごとの平均'), (329, '条件ごとの平均')]:
    ax.text(270, y, label, ha='center', va='center', fontsize=28,
            color=BLUE if y == 329 else '#000000', weight='bold' if y == 329 else 'normal')
for start, end in [(82, 145), (220, 287)]:
    ax.annotate('', xy=(270, end), xytext=(270, start),
                arrowprops={'arrowstyle': '->', 'color': GRAY, 'lw': 1.6})
ax.text(325, 117, '平均', va='center', fontsize=24)
ax.text(325, 258, '3機分を平均', va='center', fontsize=22)
save(fig, 'flight-averaging.svg')

# Condition means. Aircraft-level values are displayed separately as individual dots.
means = {condition: sum(float(row['mean_distance_m']) for row in rows if row['condition'] == condition) / 3
         for condition in 'ABC'}


def distance_chart(conditions, filename, compact=False):
    fig, ax = plt.subplots(figsize=(5.4, 4.3) if compact else (11.5, 4.3), dpi=100)
    fig.subplots_adjust(left=0.14 if compact else 0.07, right=0.97,
                        bottom=0.19 if compact else 0.16, top=0.85)
    ax.set_ylim(0, 8)
    ax.set_xlim(-0.6, len(conditions) - 0.4)
    ax.set_yticks([0, 2, 4, 6, 8])
    ax.set_axisbelow(True)
    ax.spines[['top', 'right', 'left']].set_visible(False)
    ax.spines['bottom'].set_color('#999999')
    ax.tick_params(axis='both', length=0, pad=10, labelsize=24)
    labels = {c: f'{c}：{wing_spans[c]} cm' for c in 'ABC'}
    for x, condition in enumerate(conditions):
        mean = means[condition]
        color = BLUE if condition == 'B' else GRAY
        ax.bar(x, mean, width=0.58, color=BLUE if condition == 'B' else '#a4aab1',
               edgecolor='none')
        ax.text(x, mean + 0.23, f'{mean:.1f}', ha='center', va='bottom',
                color=color, fontsize=28, weight='bold' if condition == 'B' else 'normal')
    ax.set_xticks(range(len(conditions)),
                  [labels[c].replace('：', '\n') if compact else labels[c] for c in conditions])
    fig.text(0.03, 0.935, '平均飛距離（m）', fontsize=24)
    fig.text(0.97, 0.935, '条件：翼幅', fontsize=22, ha='right', color=GRAY)
    save(fig, filename)


distance_chart('ABC', 'flight-results.svg')
distance_chart('BC', 'flight-comparison.svg', compact=True)
distance_chart('ABC', 'flight-summary.svg', compact=True)

# One dot per aircraft. No joining lines: aircraft are not paired or sequential.
fig, ax = plt.subplots(figsize=(11.5, 4.3), dpi=100)
fig.subplots_adjust(left=0.21, right=0.78, bottom=0.24, top=0.83)
ax.set(xlim=(3, 7.5), ylim=(-0.4, 2.4))
ax.set_xticks([3, 4, 5, 6, 7])
ax.set_yticks([2, 1, 0], [f'{c}  {wing_spans[c]} cm' for c in 'ABC'])
ax.spines[['top', 'right', 'left']].set_visible(False)
ax.spines['bottom'].set_color('#999999')
ax.tick_params(axis='both', length=0, pad=12, labelsize=24)
for condition, y in zip('ABC', [2, 1, 0]):
    values = [float(row['mean_distance_m']) for row in rows if row['condition'] == condition]
    color = BLUE if condition == 'B' else GRAY
    ax.scatter(values, [y] * 3, s=240, facecolors=color if condition == 'B' else 'white',
               edgecolors=color if condition != 'B' else 'none', linewidths=1.8, zorder=3)
    ax.text(7.8, y, f'{min(values):.1f}–{max(values):.1f}', va='center', fontsize=25,
            color=color, weight='bold' if condition == 'B' else 'normal', clip_on=False)
fig.text(0.21, 0.935, '1点は1機の5試行平均', fontsize=22)
fig.text(0.03, 0.935, '翼幅', fontsize=24)
fig.text(0.82, 0.935, '範囲（m）', fontsize=22)
fig.text(0.495, 0.025, '平均飛距離（m）', fontsize=24, ha='center')
save(fig, 'aircraft-results.svg')

# Introductory shape comparison: no performance or dimensions are implied.
fig, ax = diagram(height=430)
for x, width, label in [(145, 45, '小さい翼幅'), (395, 90, '大きい翼幅')]:
    plane(ax, x, width, top=45, bottom=315)
    ax.annotate('', xy=(x - width, 344), xytext=(x + width, 344),
                arrowprops={'arrowstyle': '<->', 'color': BLUE, 'lw': 1.6,
                            'shrinkA': 0, 'shrinkB': 0})
    ax.text(x, 396, label, ha='center', fontsize=24)
save(fig, 'wing-shapes.svg')

# The cover uses the same schematic drawing as the experimental figures.
fig, ax = diagram(width=340, height=475)
plane(ax, 170, 135, top=25, bottom=430)
save(fig, 'cover-airplane.svg')

# Hypothesis-generating features. The center-of-gravity marker is schematic.
fig, ax = diagram()
plane(ax, 255, 95, top=35, bottom=337)
ax.plot(255, 205, 'o', color=BLUE, markersize=10, markeredgecolor='white', markeredgewidth=1.5)
for label, start, end in [
    ('翼', (425, 138), (295, 237)),
    ('重心', (60, 202), (246, 205)),
    ('折り目', (414, 324), (263, 287)),
]:
    ax.annotate(label, xy=end, xytext=start, ha='center', va='center', fontsize=22,
                arrowprops={'arrowstyle': '-', 'color': GRAY, 'lw': 1.2, 'shrinkA': 8})
save(fig, 'aircraft-factors.svg')

# Uncontrolled release conditions: arrows illustrate possible velocity vectors,
# not measured trajectories or values from the example dataset.
fig, ax = diagram(height=350)
for end, color in [((365, 45), BLUE), ((495, 180), '#777777')]:
    ax.annotate('', xy=end, xytext=(85, 250),
                arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 2.5,
                            'mutation_scale': 20, 'shrinkA': 0, 'shrinkB': 0})
angle = PlotPath([(159, 237), (163, 222), (155, 204), (142, 208)],
                 [PlotPath.MOVETO, PlotPath.CURVE4, PlotPath.CURVE4, PlotPath.CURVE4])
ax.add_patch(PathPatch(angle, facecolor='none', edgecolor=GRAY, linewidth=1.5))
ax.plot(85, 250, 'o', color=BLUE, markersize=8)
ax.text(178, 239, '角度', fontsize=26)
ax.text(346, 156, '速さ', fontsize=26)
ax.text(25, 316, '投げる位置', fontsize=24)
save(fig, 'throw-variation.svg')

# A future repeat of the original comparison with a common center-of-gravity position.
fig, ax = diagram(height=440)
scale = 240 / BODY_LENGTH_CM
for x, condition in zip([85, 265, 445], 'ABC'):
    span = wing_spans[condition]
    plane(ax, x, span * scale / 2, top=65, bottom=305)
    ax.plot(x, 202, 'o', color=BLUE, markersize=10, markeredgecolor='white', markeredgewidth=1.5)
    ax.text(x, 24, condition, ha='center', va='center', fontsize=25, weight='bold')
    ax.text(x, 356, f'{span} cm', ha='center', va='center', fontsize=26)
ax.text(270, 410, '● 重心の位置', ha='center', va='center', fontsize=24, color=BLUE)
save(fig, 'controlled-retest.svg')
