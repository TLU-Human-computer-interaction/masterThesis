#!/usr/bin/env python3

print("Hello world!")
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

plt.figure(figsize=(15,20))

plt.barh(component, true_violations, fill=False, hatch='///')
plt.barh(component, false_violations,  left=true_violations , fill=False, hatch='/')

plt.barh(component, true_passes, left=violations, fill=False, hatch='xxx')
plt.barh(component, false_passes, left=violations_true_pass, fill=False, hatch='x')



# plt.title('Violations per component', fontsize=14)
plt.ylabel('Component', fontsize=14)
plt.xlabel('Violations', fontsize=14)


plt.savefig("src/thesis/graphs/audit.svg")
plt.savefig("src/thesis/graphs/audit.png")
