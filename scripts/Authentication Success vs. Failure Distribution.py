import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (Ensure the correct file path)
iot_data = pd.read_excel("IoT.xlsx")

# Calculate authentication success vs failure distribution
auth_success_rate = iot_data["Transaction_Status"].value_counts(normalize=True) * 100

# Generate the plot
plt.figure(figsize=(8, 5))
sns.barplot(x=auth_success_rate.index, y=auth_success_rate.values, palette="viridis")
plt.xlabel("Authentication Status")
plt.ylabel("Percentage (%)")
plt.title("Figure 2: Authentication Success vs. Failure Distribution")
plt.ylim(0, 100)

# Save and show the figure
plt.savefig("authentication_success_vs_failure.png", dpi=300)
plt.show()
