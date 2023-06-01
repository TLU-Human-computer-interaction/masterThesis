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
df = df.sort_values(['all_checks', 'true_passes'], ascending=False)

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
fig, ax = plt.subplots(figsize=(25, 10))  # Adjusted the figure size

red = '#FF696D'
lightRed = '#FFC2C4'
darkRed = "#AA282C"
green = '#6CB9AD'
lightGreen = '#ACD7D2'
darkGreen = '#20796B'

barWidth = 0.7  # Changed to barWidth instead of barHeight
edgeColor = 'black'

plt.bar(component, true_violations, hatch='///',
        label='Valid violations', color=red, edgecolor=darkRed, width=barWidth)  # Modified to plt.bar

plt.bar(component, false_violations, bottom=true_violations, hatch='/',
        label='Invalid violations', color=lightRed, edgecolor=darkRed, width=barWidth)  # Modified to plt.bar

plt.bar(component, true_passes, bottom=violations, hatch='xxx',
        label='Valid passes', color=green, edgecolor=darkGreen, width=barWidth)  # Modified to plt.bar

plt.bar(component, false_passes, bottom=violations_true_pass, hatch='x',
        label='Invalid passes', color=lightGreen, edgecolor=darkGreen, width=barWidth)  # Modified to plt.bar

# set spines visibility to False
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_color('white')
ax.spines["left"].set_color('white')

# Set x-axis and y-axis label color to white
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')


# set grids
ax.yaxis.grid(True, color='#D9D9D9')  # Changed y-axis grid visibility
ax.xaxis.grid(False)  # Changed x-axis grid visibility
ax.margins(0, tight=True)


# set labels
plt.xlabel('Component', fontsize=14)  # Swapped x-axis label
plt.ylabel('Violations', fontsize=14)  # Swapped y-axis label

# set font size for tick labels
plt.xticks(fontsize=16, color='white')
ticks = [i + barWidth / 2 for i in range(len(component))]
plt.xticks(ticks, component, rotation=45, ha='right', color='white')

# Set color of ticks on the x-axis and y-axis to white
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')


plt.savefig("src/thesis/graphs/presentation-graph.svg",
            bbox_inches='tight', pad_inches=0, transparent=True)
plt.savefig("src/thesis/graphs/presentation-graph.png",
            bbox_inches='tight', pad_inches=0, transparent=True)
