import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (Ensure correct file path)
iot_data = pd.read_excel("IoT_with_Attack_Types.xlsx")

# Convert timestamp to datetime and sort data
iot_data["Timestamp"] = pd.to_datetime(iot_data["Timestamp"])
iot_data = iot_data.sort_values(by="Timestamp")

# Calculate rolling success rate over time (window size: 10 transactions)
iot_data["Success_Rate"] = iot_data["Transaction_Status"].apply(lambda x: 1 if x == "Success" else 0)
iot_data["Rolling_Success_Rate"] = iot_data["Success_Rate"].rolling(window=10, min_periods=1).mean() * 100

# Generate Figure 2
plt.figure(figsize=(10, 5))
sns.lineplot(x=iot_data["Timestamp"], y=iot_data["Rolling_Success_Rate"], marker="o", linestyle="-")

# Fix clipping issue
plt.xlabel("Time")
plt.ylabel("Success Rate (%)")
plt.title("Figure 2: Authentication Success Trends Over Time")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()  # Adjusts layout to prevent clipping
plt.subplots_adjust(bottom=0.2)  # Adds extra padding to the bottom

# Save and show figure
plt.savefig("authentication_success_trends.png", dpi=300, bbox_inches="tight")
plt.show()
