import pandas as pd

# Load the dataset
iot_data = pd.read_excel("IoT_with_Attack_Types.xlsx")  # Ensure correct file path

# Convert timestamp column to datetime
iot_data["Timestamp"] = pd.to_datetime(iot_data["Timestamp"])

# Sort dataset by timestamp (to ensure proper ordering)
iot_data = iot_data.sort_values(by="Timestamp")

# Calculate transaction latency (time difference between consecutive transactions)
iot_data["Latency"] = iot_data["Timestamp"].diff().dt.total_seconds().fillna(0)

# Compute key performance metrics again
avg_latency = iot_data["Latency"].mean()
max_latency = iot_data["Latency"].max()
min_latency = iot_data["Latency"].min()
avg_gas_fee = iot_data["Gas_Fee_ETH"].mean()
success_rate = (iot_data["Transaction_Status"] == "Success").mean() * 100

# Print corrected values
print(f"Corrected Average Transaction Latency: {avg_latency:.2f} seconds")
print(f"Corrected Maximum Latency: {max_latency:.2f} seconds")
print(f"Corrected Minimum Latency: {min_latency:.2f} seconds")
print(f"Corrected Average Gas Fee per Transaction: {avg_gas_fee:.6f} ETH")
print(f"Transaction Success Rate: {success_rate:.2f}%")
