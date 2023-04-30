#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd

usecols = ["component", "violations", "true_violations", "passes", "true_passes"]

# Read the CSV file
audit_data = pd.read_csv("src/thesis/graphs/data.csv", header=0, usecols=usecols)
df = pd.DataFrame(audit_data)
# Calculated fields
df['false_violations']= df.violations - df.true_violations
df['false_passes']= df.passes - df.true_passes
df['all_checks']= df.violations + df.passes
# Sort data
df = df.sort_values('all_checks')

color_dict = {'true_violations': '#FF696D',
              'false_violations': '#FFC2C4',
              'true_passes': '#6CB9AD',
              'false_passes': '#ACD7D2'}

ax = df.plot(kind='barh',
             x=0,
             y=['true_violations', 'false_violations', 'true_passes', 'false_passes'],
             figsize=(10,15),
             title='Violations per component',
             xlabel='Violations',
             ylabel='Component',
             fontsize=10,
             stacked=True,
             color=['#FF696D', '#FFC2C4', '#6CB9AD', '#ACD7D2'],
             )

ax.autoscale()
# ax.barh(component, true_violations, color='#FF696D')
# ax.barh(component, false_violations, left=true_violations, color='#FFC2C4')


# annotate
# ax.bar_label(ax.containers[1], label_type='edge')
# ax.bar_label(ax.containers[1], label_type='edge')
# ax.bar_label(ax.containers[0])

# Save the chart so we can loop through the bars below.
# bars = ax.barh(
#     width=violations,
#     tick_label=component('%Y')
# )

# Axis formatting.
# remove the top, right and left spines (figure borders)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
# make the bottom spine gray instead of black.
ax.spines['bottom'].set_color('#DDDDDD')
# remove the ticks as well.
ax.tick_params(bottom=False, left=False)
# Third, add a vertical grid (but keep the horizontal grid hidden).
ax.set_axisbelow(True)
ax.yaxis.grid(False)
# Color the lines a light gray as well.
ax.xaxis.grid(True, color='#EEEEEE')

# for bar in bars:
#   ax.text(
#       bar.get_x() + bar.get_width() / 2,
#       bar.get_height() + 0.3,
#       round(bar.get_height(), 1),
#       horizontalalignment='center',
#       color=bar_color,
#       weight='bold'
#   )

# def addlabels(x, y):
#     print(y)
#     for i in range(len(y)):
#         # print(y)
#         # plt.text(i,y[i],y[i])
#         plt.text(i,'x','y')

# addlabels(component, violations)

# plt.savefig("src/thesis/graphs/test.png")
plt.savefig("src/thesis/graphs/test.svg")
