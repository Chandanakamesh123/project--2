import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# Title
# =====================================================

st.title("Factory-to-Customer Shipping Route Efficiency Analysis")

st.write("Logistics and Shipment Performance Dashboard")


# =====================================================
# Load Dataset
# =====================================================

df = pd.read_csv('processed_shipping_data.csv')


# =====================================================
# Display Dataset
# =====================================================

st.subheader("Processed Shipping Dataset")

st.dataframe(df)


# =====================================================
# Shipment Mode Analysis
# =====================================================

st.subheader("Shipment Mode Analysis")

shipment_counts = df['Shipment_Mode'].value_counts()

fig, ax = plt.subplots()

shipment_counts.plot(kind='bar', ax=ax)

plt.xlabel("Shipment Mode")

plt.ylabel("Count")

plt.title("Shipment Mode Distribution")

st.pyplot(fig)


# =====================================================
# Delivery Status Analysis
# =====================================================

st.subheader("Delivery Status Analysis")

delivery_counts = df['Delivery_Status'].value_counts()

fig2, ax2 = plt.subplots()

delivery_counts.plot(
    kind='pie',
    autopct='%1.1f%%',
    ax=ax2
)

plt.title("Delivery Status Distribution")

st.pyplot(fig2)


# =====================================================
# Vendor Performance
# =====================================================

st.subheader("Vendor Performance")

vendor_counts = df['Vendor'].value_counts()

fig3, ax3 = plt.subplots()

vendor_counts.plot(kind='bar', ax=ax3)

plt.xlabel("Vendor")

plt.ylabel("Count")

plt.title("Vendor Shipment Count")

st.pyplot(fig3)


# =====================================================
# Delay Prediction Section
# =====================================================

st.subheader("Shipment Delay Insights")

average_delay = df['Delay_Days'].mean()

st.write(f"Average Delay Days: {average_delay:.2f}")


# =====================================================
# Conclusion
# =====================================================

st.success(
    "Dashboard Loaded Successfully"
)
