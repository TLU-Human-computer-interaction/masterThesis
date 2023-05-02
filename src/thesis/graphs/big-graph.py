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
df['violations_true_pass'] = df.violations + df.true_passes

# Sort data
df = df.sort_values('all_checks')

component = list(df.iloc[:, 0])
violations = list(df.iloc[:, 1])
true_violations = list(df.iloc[:, 2])
passes = list(df.iloc[:, 3])
true_passes = list(df.iloc[:, 4])
false_violations = list(df.iloc[:, 5])
false_passes = list(df.iloc[:, 6])
all_checks = list(df.iloc[:, 7])
violations_true_pass = list(df.iloc[:, 8])

print(df.head())

# create plot
fig, ax = plt.subplots(figsize=(15,25))

bar_height = 0.7

plt.barh(component, true_violations, fill=False, hatch='///', label='Valid violations', height=bar_height)
plt.barh(component, false_violations,  left=true_violations , fill=False, hatch='/', label='Invalid violations', height=bar_height)

plt.barh(component, true_passes, left=violations, fill=False, hatch='xxx', label='Valid passes', height=bar_height)
plt.barh(component, false_passes, left=violations_true_pass, fill=False, hatch='x', label='Invalid passes', height=bar_height)

# set spines visibility to False
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
# ax.spines["left"].set_visible(False)

#  set grids
ax.yaxis.grid(False)
ax.xaxis.grid(True, color='#D9D9D9')

# set labels
plt.ylabel('Component', fontsize=14)
plt.xlabel('Violations', fontsize=14)

# set font size for y-axis tick labels
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)

# add legend
plt.legend(loc='lower right', fontsize=16)

# remove vertical space between bars and spines
ax.margins(0)

# adjust the left margin
fig.subplots_adjust(left=0.2)

# save the plot with trim
plt.savefig("src/thesis/graphs/audit.svg", bbox_inches='tight', pad_inches=0 )
plt.savefig("src/thesis/img/audit/combined_bw.png", bbox_inches='tight', pad_inches=0)

