# analysis.py
import matplotlib.pyplot as plt

# Quarterly CAC data
quarters = ["Q1", "Q2", "Q3", "Q4"]
cac_values = [226.49, 230.66, 231.59, 231.17]
average_cac = sum(cac_values) / len(cac_values)

# Industry benchmark
industry_target = 150
hello=100

# Print key stats
print(f"Quarterly CAC values: {cac_values}")
print(f"Average CAC: {average_cac:.2f}")
print(f"Industry Target CAC: {industry_target}")

# Plot CAC trend vs industry target
plt.figure(figsize=(8,5))
plt.plot(quarters, cac_values, marker='o', linestyle='-', color='blue', label='CAC')
plt.axhline(industry_target, color='red', linestyle='--', label='Industry Target')
plt.title('Quarterly Customer Acquisition Cost (CAC) vs Industry Target')
plt.ylabel('CAC ($)')
plt.xlabel('Quarter')
plt.grid(True)
plt.legend()
plt.savefig("cac_trend.png")
plt.show()

