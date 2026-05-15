import pandas as pd

# Load dataset
df = pd.read_csv('dataset/raw_shipping_data.csv')

# Remove missing values
df.dropna(inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert date columns
df['Scheduled_Delivery_Date'] = pd.to_datetime(
    df['Scheduled_Delivery_Date']
)

df['Actual_Delivery_Date'] = pd.to_datetime(
    df['Actual_Delivery_Date']
)

# Save cleaned dataset
df.to_csv('dataset/processed_shipping_data.csv', index=False)

print("Data cleaning completed successfully")
