import json
import joblib
import pandas as pd
import streamlit as st
from pathlib import Path

MODEL_DIR = Path("models")


@st.cache_resource
def load_artifacts():
    try:
        model = joblib.load(
            MODEL_DIR / "champion.joblib"
        )

        feature_cols = json.loads(
            (MODEL_DIR / "feature_cols.json").read_text()
        )

        return model, feature_cols

    except FileNotFoundError:
        st.error(
            "❌ Model files not found. Please ensure champion.joblib and feature_cols.json exist in the models folder."
        )
        st.stop()


def predict_yield(
    temperature_c: float,
    humidity_pct: float,
    co2_ppm: float
) -> float:

    model, feature_cols = load_artifacts()

    row = pd.DataFrame(
        [[
            temperature_c,
            humidity_pct,
            co2_ppm
        ]],
        columns=feature_cols
    )

    prediction = model.predict(row)

    return float(prediction[0])


if __name__ == "__main__":
    result = predict_yield(
        22.0,
        88.0,
        920.0
    )

    print(f"Predicted Yield: {result:.2f} kg")