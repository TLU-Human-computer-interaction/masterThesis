import matplotlib.pyplot as plt

# Define data
# title = "Do you know where to find resources about accessibility standards?"
# file = 'resources-pie'
# labels = ['Yes', 'Yes, but I think\nI need more', 'No', "No I don't think I need them"]
# values = [7, 10, 3, 0]
title = "Do you know where to find resources about accessibility standards?"
file = 'test-knowledge-pie'
labels = ["Yes", "Yes, but I think what\nI use now is not enough",
    "No", "No I don't think we need to test theaccessibility of our product"]
values = [5, 8, 7, 0]

# Define patterns
patterns = ['/', 'o', '+', '.']
colors = ['#6CB9AD', '#EDC161', '#FF696D', '#5D45DB']

# Filter out empty values
nonzero_values = [size for size in values if size != 0]
nonzero_labels = [label for label, size in zip(labels, values) if size != 0]


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        print(pct, val)
        return '{p:.1f}%  ({v:d})'.format(p=pct, v=val)
    return my_autopct


# Create pie chart
# fig, ax = plt.subplots()
# wedges, _, percent = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
#                       wedgeprops={'linewidth': 1, 'fill':False, 'hatch': patterns})
fig, ax = plt.subplots()
wedges, _, percent = ax.pie(nonzero_values, labels=nonzero_labels, autopct=make_autopct(nonzero_values), startangle=90, colors=colors,
                            wedgeprops={'linewidth': 1, 'edgecolor': 'white', })


# Apply patterns to wedges
# for wedge, pattern in zip(wedges, patterns):
#     wedge.set_hatch(pattern)

for label, value, wedge in zip(_, percent, wedges):
    # wedge.set_text('{} {}'.format(value.get_text(), label.get_text()))
    print(wedge.get_label())
    # print(label.get_text())


# Add title
# plt.title(title)

# save the plot with trim
plt.savefig("src/thesis/graphs/{}.svg".format(file),
            bbox_inches='tight', pad_inches=0)
plt.savefig("src/thesis/img/surveys/{}.png".format(file),
            bbox_inches='tight', pad_inches=0)
