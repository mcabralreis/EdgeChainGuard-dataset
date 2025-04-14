import pandas as pd

# Load dataset
blockchain_data = pd.read_excel("blockchain.xlsx")  # Ensure correct file path

# Generate summary statistics for Gas_Fee_ETH
gas_fee_summary = blockchain_data["Gas_Fee_ETH"].describe()

# Print all values clearly
print(f"\nFinal Blockchain Gas Fee Summary:")
print(f"Count: {gas_fee_summary['count']:.0f}")
print(f"Mean: {gas_fee_summary['mean']:.6f} ETH")
print(f"Std Dev: {gas_fee_summary['std']:.6f} ETH")
print(f"Min: {gas_fee_summary['min']:.6f} ETH")
print(f"25%: {gas_fee_summary['25%']:.6f} ETH")
print(f"50% (Median): {gas_fee_summary['50%']:.6f} ETH")
print(f"75%: {gas_fee_summary['75%']:.6f} ETH")
print(f"Max: {gas_fee_summary['max']:.6f} ETH")
