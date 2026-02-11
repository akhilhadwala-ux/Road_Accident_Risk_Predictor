
## 📌 Overview

This dataset contains road and environmental conditions along with accident-related information.
It can be used for building machine learning models to **predict accident risk** or analyze factors influencing road safety.

The dataset contains:

* **517,754 rows**
* **14 columns**
* Mixed data types (categorical, numerical, and boolean)


## 📊 Column Description

| Column Name              | Description                                                           |
| ------------------------ | --------------------------------------------------------------------- |
| `id`                     | Unique identifier for each record                                     |
| `road_type`              | Type of road (urban, rural, highway)                                  |
| `num_lanes`              | Number of lanes on the road                                           |
| `curvature`              | Road curvature value (numeric measure of how curved the road is)      |
| `speed_limit`            | Speed limit of the road (in km/h or mph depending on dataset context) |
| `lighting`               | Lighting condition (e.g., daylight, dim)                              |
| `weather`                | Weather condition (clear, rainy, foggy, etc.)                         |
| `road_signs_present`     | Whether road signs are present (True/False)                           |
| `public_road`            | Whether the road is public (True/False)                               |
| `time_of_day`            | Time period (morning, afternoon, evening)                             |
| `holiday`                | Whether the day is a holiday (True/False)                             |
| `school_season`          | Whether schools are in session (True/False)                           |
| `num_reported_accidents` | Number of reported accidents at that location/time                    |
| `accident_risk`          | Calculated accident risk score (Target variable)                      |


## 🎯 Target Variable

`accident_risk`

This column represents the accident risk score.
It can be used as:

* A **regression target** (predict risk score)
* A **classification target** (if converted into low/medium/high risk categories)


## 💡 Possible Use Cases

* Predict accident risk based on road and weather conditions
* Analyze impact of curvature and speed limits on safety
* Study effect of lighting and weather on accidents
* Build safety recommendation systems
* Perform exploratory data analysis (EDA)


## 🛠 Suggested Workflow

1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Encoding (for categorical variables)
4. Model Building (Regression)
5. Model Evaluation
6. Deployment (optional)


## 📎 Notes

* The dataset contains both categorical and numerical features.
* Boolean columns may need conversion to 0/1 for modeling.
* Feature scaling may help in some machine learning algorithms.


