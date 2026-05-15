import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv('dataset/processed_shipping_data.csv')

# Features and Target
X = df[['Shipping_Cost', 'Distance_km']]

y = df['Delay_Days']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()

model.fit(X_train, y_train)

print("Model training completed")
