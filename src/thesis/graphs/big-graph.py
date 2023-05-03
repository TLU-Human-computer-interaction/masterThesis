#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd

usecols = ["component", "violations",
           "true_violations", "passes", "true_passes"]

# Read the CSV file
audit_data = pd.read_csv("src/thesis/graphs/data.csv",
                         header=0, usecols=usecols)
df = pd.DataFrame(audit_data)

# Calculated fields
df['false_violations'] = df.violations - df.true_violations
df['false_passes'] = df.passes - df.true_passes
df['all_checks'] = df.violations + df.passes
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
fig, ax = plt.subplots(figsize=(15, 25))


red = '#FF696D'
lightRed = '#FFC2C4'
darkRed = "#AA282C"
green = '#6CB9AD'
lightGreen = '#ACD7D2'
darkGreen = '#20796B'

barHeight = 0.7
edgeColor = 'black'

plt.barh(component, true_violations, hatch='///',
         label='Valid violations', color=red, edgecolor=darkRed, height=barHeight)
plt.barh(component, false_violations,  left=true_violations, hatch='/',
         label='Invalid violations', color=lightRed, edgecolor=darkRed, height=barHeight)

plt.barh(component, true_passes, left=violations, hatch='xxx',
         label='Valid passes', color=green, edgecolor=darkGreen, height=barHeight)

plt.barh(component, false_passes, left=violations_true_pass, hatch='x',
         label='Invalid passes', color=lightGreen, edgecolor=darkGreen, height=barHeight)


# set spines visibility to False
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

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
plt.savefig("src/thesis/graphs/audit.svg", bbox_inches='tight', pad_inches=0)
plt.savefig("src/thesis/img/audit/combined_bw.png",
            bbox_inches='tight', pad_inches=0)
