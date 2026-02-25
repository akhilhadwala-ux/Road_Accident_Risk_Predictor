## 📌 Overview

The **Road Accident Risk Predictor** is a machine learning project designed to analyze road and environmental conditions to predict accident risk levels.  

This project demonstrates the application of data science and predictive modeling techniques to improve road safety analysis and decision-making.

The dataset contains:

- **517,754 rows**
- **14 columns**
- Mixed data types (categorical, numerical, and boolean)

---

## 📊 Dataset Description

The dataset includes road characteristics, environmental conditions, and accident-related metrics.

| Column Name | Description |
|-------------|------------|
| `id` | Unique identifier for each record |
| `road_type` | Type of road (urban, rural, highway) |
| `num_lanes` | Number of lanes on the road |
| `curvature` | Road curvature value (numeric measure of curvature) |
| `speed_limit` | Speed limit of the road |
| `lighting` | Lighting condition (daylight, dim, etc.) |
| `weather` | Weather condition (clear, rainy, foggy, etc.) |
| `road_signs_present` | Whether road signs are present (True/False) |
| `public_road` | Whether the road is public (True/False) |
| `time_of_day` | Morning, afternoon, evening |
| `holiday` | Whether the day is a holiday (True/False) |
| `school_season` | Whether schools are in session (True/False) |
| `num_reported_accidents` | Number of reported accidents |
| `accident_risk` | Calculated accident risk score (Target Variable) |

---

## 🎯 Target Variable

### `accident_risk`

This variable represents the accident risk score and can be used as:

- **Regression Target** → Predict continuous risk score  
- **Classification Target** → Categorize into Low / Medium / High risk  

---

## 💡 Project Objectives

- Predict accident risk using structured tabular data  
- Analyze the impact of road curvature and speed limits  
- Study how lighting and weather influence safety  
- Build a deployable ML model for real-world risk assessment  
- Perform exploratory data analysis (EDA) to uncover insights  

---

## 🛠️ Project Workflow

1. **Data Cleaning**
2. **Exploratory Data Analysis (EDA)**
3. **Feature Engineering & Encoding**
4. **Model Building (Regression)**
5. **Model Evaluation**
6. **Deployment using Hugging Face Spaces**

---

## 🚀 Deployment

The trained model is deployed as an interactive web application using **Hugging Face Spaces**.

👉 Try the live demo here:  
https://huggingface.co/spaces/Akhil-Hadwala/Road_Accident_Risk_Prediction

---

## 📎 Technical Notes

- Dataset contains categorical, numerical, and boolean features  
- Boolean variables are converted to 0/1 for modeling  
- Feature scaling applied where necessary  
- Suitable for regression and classification approaches  

---

## 👨‍💻 Author

**Akhil Hadwala**  
Machine Learning & AI Enthusiast  
Focused on real-world predictive modeling and deployment.

