import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the updated dataset (Ensure the correct file path)
iot_data = pd.read_excel("IoT_with_Attack_Types.xlsx")

# Generate attack distribution plot
plt.figure(figsize=(8, 5))
sns.countplot(x="Attack_Type", data=iot_data, palette="magma", order=iot_data["Attack_Type"].value_counts().index)
plt.xlabel("Attack Type")
plt.ylabel("Count")
plt.title("Figure 3: Attack Simulation Breakdown")

# Save and show the figure
plt.savefig("attack_simulation_distribution.png", dpi=300)
plt.show()
