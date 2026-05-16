import pandas as pd
import matplotlib.pyplot as plt

# Load processed dataset
df = pd.read_csv('processed_shipping_data.csv')

# Shipment Mode Analysis
print(df['Shipment_Mode'].value_counts())

# Vendor Analysis
print(df['Vendor'].value_counts())

# Delivery Status Analysis
print(df['Delivery_Status'].value_counts())

# Shipment Mode Bar Chart
df['Shipment_Mode'].value_counts().plot(kind='bar')

plt.title("Shipment Mode Analysis")

plt.xlabel("Shipment Mode")

plt.ylabel("Count")

plt.show()
