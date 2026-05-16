import pandas as pd

# Load dataset
df = pd.read_csv('processed_shipping_data.csv')

# Convert dates
df['Scheduled_Delivery_Date'] = pd.to_datetime(
    df['Scheduled_Delivery_Date']
)

df['Actual_Delivery_Date'] = pd.to_datetime(
    df['Actual_Delivery_Date']
)

# Create Delay_Days column
df['Delay_Days'] = (
    df['Actual_Delivery_Date']
    - df['Scheduled_Delivery_Date']
).dt.days

# Create Efficiency Score
df['Efficiency_Score'] = 100 - (df['Delay_Days'] * 10)

# Save updated dataset
df.to_csv('processed_shipping_data.csv', index=False)

print("Feature engineering completed")
