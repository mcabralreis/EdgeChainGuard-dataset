import pandas as pd
import numpy as np

# Load the existing dataset
iot_data = pd.read_excel("IoT.xlsx")  # Ensure the correct file path

# Define possible attack types
attack_types = ["Brute Force", "DDoS", "Spoofing", "Malicious Smart Contract", "None"]

# Create a new column for attack types
iot_data["Attack_Type"] = iot_data["Transaction_Status"].apply(
    lambda x: np.random.choice(attack_types[:-1]) if x == "Failed" else "None"
)

# Save the updated dataset
iot_data.to_excel("IoT_with_Attack_Types.xlsx", index=False)

print("Updated dataset saved as IoT_with_Attack_Types.xlsx")
