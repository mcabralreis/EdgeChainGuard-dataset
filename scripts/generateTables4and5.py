import pandas as pd

# Load dataset (Ensure correct file path)
iot_data = pd.read_excel("IoT_with_Attack_Types.xlsx")

# Convert timestamp column to datetime
iot_data["Timestamp"] = pd.to_datetime(iot_data["Timestamp"])

# Sort dataset by timestamp (to ensure proper ordering)
iot_data = iot_data.sort_values(by="Timestamp")

# Calculate transaction latency (time difference between consecutive transactions)
iot_data["Latency"] = iot_data["Timestamp"].diff().dt.total_seconds().fillna(0)

# Compute authentication success rate as a percentage
iot_data["Success_Rate"] = iot_data["Transaction_Status"].apply(lambda x: 1 if x == "Success" else 0)

# Generate IoT Authentication Summary
iot_summary = iot_data[["Latency", "Success_Rate"]].describe().T

# Print IoT Authentication Data Summary
print("\nCorrected IoT Authentication Data Summary:\n", iot_summary)
