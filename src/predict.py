import json
import joblib
import pandas as pd
from pathlib import Path

MODEL_DIR = Path("models")

# Load champion model
_model = joblib.load(
    MODEL_DIR / "champion.joblib"
)

# Load feature order
_feature_cols = json.loads(
    (MODEL_DIR / "feature_cols.json").read_text()
)


def predict_yield(
    temperature_c: float,
    humidity_pct: float,
    co2_ppm: float
) -> float:
    """
    Predict crop yield in kg.
    """

    # Create DataFrame with correct feature names
    row = pd.DataFrame(
        [[
            temperature_c,
            humidity_pct,
            co2_ppm
        ]],
        columns=_feature_cols
    )

    prediction = _model.predict(row)

    return float(prediction[0])


if __name__ == "__main__":
    result = predict_yield(
        22.0,   # temperature
        88.0,   # humidity
        920.0   # CO2
    )

    print(f"Predicted Yield: {result:.2f} kg")