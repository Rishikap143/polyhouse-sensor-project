import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
from pathlib import Path
from src.predict import predict_yield


# Prediction logging
def log_prediction(temp, humidity, co2, prediction):
    log_file = "prediction_log.csv"

    row = pd.DataFrame([{
        "timestamp": datetime.now(),
        "temperature": temp,
        "humidity": humidity,
        "co2": co2,
        "prediction": prediction
    }])

    if Path(log_file).exists():
        row.to_csv(
            log_file,
            mode="a",
            header=False,
            index=False
        )
    else:
        row.to_csv(
            log_file,
            index=False
        )


# Page setup
st.set_page_config(
    page_title="Polyhouse Yield Predictor",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 Polyhouse Yield Predictor")
st.caption("Agritech environmental forecasting from sensor data")

# Sidebar inputs
with st.sidebar:
    st.header("Sensor Readings")

    temp = st.slider(
        "Temperature (°C)",
        min_value=10.0,
        max_value=35.0,
        value=22.0,
        step=0.1
    )

    humid = st.slider(
        "Humidity (%)",
        min_value=50.0,
        max_value=100.0,
        value=88.0,
        step=0.5
    )

    co2 = st.slider(
        "CO₂ (ppm)",
        min_value=400,
        max_value=2000,
        value=900,
        step=10
    )

# Warnings
if temp > 32:
    st.warning("⚠ High temperature detected")

if humid < 60:
    st.warning("⚠ Low humidity detected")

if co2 > 1800:
    st.warning("⚠ High CO₂ level detected")

# Prediction
if st.button("Predict Yield"):

    with st.spinner("Generating prediction..."):

        kg = predict_yield(
            temp,
            humid,
            co2
        )

        log_prediction(
            temp,
            humid,
            co2,
            kg
        )

    st.metric(
        label="Estimated Daily Yield",
        value=f"{kg:.2f} kg"
    )

    st.success("✅ Prediction logged successfully")

# Sensitivity Chart
st.subheader("What-if Analysis: Humidity Sweep")

temp_fixed = 22.0
co2_fixed = 900

humid_range = np.linspace(70, 98, 29)

preds = [
    predict_yield(temp_fixed, h, co2_fixed)
    for h in humid_range
]

chart_df = pd.DataFrame({
    "Humidity (%)": humid_range,
    "Predicted Yield (kg)": preds
})

st.line_chart(
    chart_df,
    x="Humidity (%)",
    y="Predicted Yield (kg)"
)

# Model metadata
with st.expander("Model Information"):
    st.markdown("""
    **Model:** Tuned Random Forest

    **Inputs:** Temperature, Humidity, CO₂

    **Output:** Yield (kg)

    **Training Data:** Polyhouse sensor dataset

    **Test MAE:** Replace with your actual MAE
    """)

st.markdown("---")
st.caption("Polyhouse Sensor Project | Task 8")