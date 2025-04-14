import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (Ensure correct file path)
iot_data = pd.read_excel("IoT_with_Attack_Types.xlsx")

# Convert timestamp to datetime and sort data
iot_data["Timestamp"] = pd.to_datetime(iot_data["Timestamp"])
iot_data = iot_data.sort_values(by="Timestamp")

# Calculate transaction latency
iot_data["Latency"] = iot_data["Timestamp"].diff().dt.total_seconds().fillna(0)

# Generate Figure 4
plt.figure(figsize=(8, 5))
sns.scatterplot(x=iot_data.index, y=iot_data["Latency"], alpha=0.6)
plt.xlabel("Transaction Index")
plt.ylabel("Latency (seconds)")
plt.title("Figure 4: Latency vs. Transaction Load")
plt.grid(True)

# Save and show figure
plt.savefig("latency_vs_transaction_load.png", dpi=300)
plt.show()
