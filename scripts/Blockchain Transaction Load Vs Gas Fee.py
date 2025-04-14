import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (Ensure correct file path)
blockchain_data = pd.read_excel("blockchain.xlsx")

# Generate scatter plot of transaction load vs. gas fee
plt.figure(figsize=(8, 5))
sns.scatterplot(x=blockchain_data.index, y=blockchain_data["Gas_Fee_ETH"], alpha=0.6, color="blue")

# Customize plot
plt.xlabel("Transaction Index (Load)")
plt.ylabel("Gas Fee (ETH)")
plt.title("Figure X: Blockchain Transaction Load vs. Gas Fee")
plt.grid(True)

# Save and show the figure
plt.savefig("blockchain_transaction_load_vs_gas_fee.png", dpi=300)
plt.show()
