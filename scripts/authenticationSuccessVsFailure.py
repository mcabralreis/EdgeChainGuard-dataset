import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the synthetic dataset
iot_data = pd.read_excel("IoT.xlsx")  # Ensure the correct file path is used

# Extract authentication success/failure rates
auth_success_rate = iot_data["Transaction_Status"].value_counts(normalize=True) * 100

# Generate a bar chart for authentication success vs failure
plt.figure(figsize=(8, 5))
sns.barplot(x=auth_success_rate.index, y=auth_success_rate.values, palette="viridis")

# Customize plot
plt.xlabel("Authentication Status")
plt.ylabel("Percentage (%)")
plt.title("Authentication Success vs. Failure in IoT Devices")
plt.ylim(0, 100)

# Show the plot
plt.show()
