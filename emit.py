import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

st.title("🌱 Carbon Footprint Estimator")

st.write("Estimate your weekly CO₂ emissions (in kg/week) based on your lifestyle.")

# User inputs
diet = st.selectbox("Your diet type:", ["Vegan", "Vegetarian", "Meat-heavy"])
diet_val = {"Vegan": 1, "Vegetarian": 2, "Meat-heavy": 3}[diet]

transport_km = st.slider("Weekly travel distance (in km):", 0, 500, 100)
electricity_kwh = st.slider("Weekly electricity usage (in kWh):", 0, 300, 150)

# Synthetic training data
np.random.seed(42)
n = 100
X = pd.DataFrame({
    'diet': np.random.randint(1, 4, size=n),
    'transport_km_week': np.random.randint(0, 500, size=n),
    'electricity_kwh_week': np.random.randint(50, 300, size=n)
})
X['co2_kg_week'] = (
    X['diet'] * 10 + 
    X['transport_km_week'] * 0.2 + 
    X['electricity_kwh_week'] * 0.5 + 
    np.random.normal(0, 10, size=n)
)

# Model Training
features = ['diet', 'transport_km_week', 'electricity_kwh_week']
model = LinearRegression()
model.fit(X[features], X['co2_kg_week'])

# Prediction for user input
user_data = pd.DataFrame([[diet_val, transport_km, electricity_kwh]], columns=features)
co2_prediction = model.predict(user_data)[0]

st.subheader("🧮 Estimated CO₂ Emission:")
st.metric(label="Your Estimated CO₂ (kg/week)", value=f"{co2_prediction:.2f}")

# To display actual vs predicted graph
if st.checkbox("Show model performance graph"):
    y_pred = model.predict(X[features])
    mse = mean_squared_error(X['co2_kg_week'], y_pred)
    st.write(f"Mean Squared Error: {mse:.2f}")

    fig, ax = plt.subplots()
    ax.scatter(X['co2_kg_week'], y_pred, alpha=0.6)
    ax.plot([X['co2_kg_week'].min(), X['co2_kg_week'].max()],
             [X['co2_kg_week'].min(), X['co2_kg_week'].max()], 'r--')
    ax.set_xlabel("Actual CO₂")
    ax.set_ylabel("Predicted CO₂")
    ax.set_title("Actual vs Predicted CO₂ Emissions")
    st.pyplot(fig)
