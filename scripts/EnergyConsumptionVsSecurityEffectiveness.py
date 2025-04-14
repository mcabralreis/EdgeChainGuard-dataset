import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
iot_data = pd.read_excel("IoT_with_Attack_Types.xlsx")

# Ensure transaction status is categorical for plotting
iot_data["Transaction_Status"] = iot_data["Transaction_Status"].astype(str)

# Generate Figure 5
plt.figure(figsize=(8, 5))
sns.boxplot(x=iot_data["Transaction_Status"], y=iot_data["Gas_Fee_ETH"], palette="magma")
plt.xlabel("Security Effectiveness (Success vs. Failed Transactions)")
plt.ylabel("Gas Fee (ETH) - Energy Cost")
plt.title("Figure 5: Energy Consumption vs. Security Effectiveness")
plt.grid(True)

# Save and show figure
plt.savefig("energy_vs_security_tradeoff.png", dpi=300)
plt.show()
