import streamlit as st
import pandas as pd
import pickle

st.title("🚧 Road Accident Risk Predictor")

st.write(
    "This app takes binary inputs (0 = No, 1 = Yes) and predicts "
    "the **accident risk score** (continuous value).")

# ---------------- Load Model (Cached) ----------------
@st.cache_resource
def load_model():
    with open("rf.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()


# ---------- Binary Inputs ----------

road_signs_present = st.selectbox("Road Signs Present:", [0, 1])
public_road = st.selectbox("Public Road:", [0, 1])
holiday = st.selectbox("Holiday Season:", [0, 1])
school_season = st.selectbox("School Season:", [0, 1])

road_type_highway = st.selectbox("Road Type = Highway:", [0, 1])
road_type_rural = st.selectbox("Road Type = Rural:", [0, 1])
road_type_urban = st.selectbox("Road Type = Urban:", [0, 1])

lighting_daylight = st.selectbox("Lighting = Daylight:", [0, 1])
lighting_dim = st.selectbox("Lighting = Dim:", [0, 1])
lighting_night = st.selectbox("Lighting = Night:", [0, 1])

weather_clear = st.selectbox("Weather = Clear:", [0, 1])
weather_foggy = st.selectbox("Weather = Foggy:", [0, 1])
weather_rainy = st.selectbox("Weather = Rainy:", [0, 1])

time_of_day_afternoon = st.selectbox("Time of Day = Afternoon:", [0, 1])
time_of_day_evening = st.selectbox("Time of Day = Evening:", [0, 1])
time_of_day_morning = st.selectbox("Time of Day = Morning:", [0, 1])

# ---------- Numeric but Binary ----------

num_lanes = st.number_input("Number of Lanes is a value between (0 or 1):")
speed_limit = st.number_input("Speed Limit is a value between (0 or 1):")
num_reported_accidents = st.number_input("Previously Reported Accidents is a value between (0 or 1):")
curvature = st.number_input("Road Curvature is a value between (0 or 1):")

# ---------- Prediction ----------

# ---------------- Prediction ----------------
if st.button("Predict Accident Risk"):
    feature_columns = [
        "road_signs_present", "public_road", "holiday", "school_season",
        "road_type_highway", "road_type_rural", "road_type_urban",
        "lighting_daylight", "lighting_dim", "lighting_night",
        "weather_clear", "weather_foggy", "weather_rainy",
        "time_of_day_afternoon", "time_of_day_evening", "time_of_day_morning",
        "num_lanes", "speed_limit", "num_reported_accidents", "curvature"
    ]


    input_data = pd.DataFrame([[
        road_signs_present, public_road, holiday, school_season,
        road_type_highway, road_type_rural, road_type_urban,
        lighting_daylight, lighting_dim, lighting_night,
        weather_clear, weather_foggy, weather_rainy,
        time_of_day_afternoon, time_of_day_evening, time_of_day_morning,
        num_lanes, speed_limit, num_reported_accidents, curvature
    ]], columns=feature_columns)

    # Regression prediction
    accident_risk = model.predict(input_data)[0]

    st.success(f"🚨 Predicted Accident Risk Score: **{accident_risk:.3f}**")