import pandas as pd

# Load dataset
blockchain_data = pd.read_excel("blockchain.xlsx")  # Ensure correct file path

# Generate summary statistics
blockchain_summary = blockchain_data.describe().T

# Print full Blockchain Data Summary
print("\nFinal Blockchain Data Summary:\n", blockchain_summary)
