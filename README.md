# The Taxi_Fare_Predictor Model

By Mahdi M. Haroun, University of Jordan, ID 0228222  
Project Related to Machine Learning with Python  
Date of Publish: 20th of Dec, 2024

---

## Overview of the Project 🚀🌍🌐

This project was created from scratch using a CSV data file from Kaggle.com (https://www.kaggle.com/datasets/denkuznetz/taxi-price-prediction) named **"Taxi Trip Pricing."** The dataset is designed to predict taxi trip fares based on various factors such as distance, time of day, traffic conditions, and more. It provides realistic synthetic data for regression tasks, offering a unique opportunity to explore pricing trends in the taxi industry. The dataset includes the following features (columns):

1. **Trip Distance**  
2. **Time of Day**  
3. **Day of Week**  
4. **Weather**  
5. **Passenger Count**  
6. **Traffic Condition**  
7. **Trip Duration**  
8. **Trip Price** (Target Variable)

---

## Data Preprocessing 📈🔧🌍

Three unnecessary columns were dropped.  
Ordinal features were encoded using a mapper for the following columns:
- **Traffic Condition**  
- **Weather**  
- **Time of Day**  
- **Day of Week**  

The CSV file contained 50 null values for each feature, which were resolved using two methods:

1. **Mean Imputation:** Applied to:
   - **Trip_Distance**  
   - **Trip_Duration_Minutes**  
   - **Trip_Price**  

2. **Random Number Generator:** Applied to:
   - **Passenger Count**  
   - **Day of Week**  
   - **Weather**  
   - **Time of Day**  
   - **Traffic Condition**  

---

## Exploratory Data Analysis (EDA) 🎨🔢🔍

A correlation plot provided an accurate heatmap (refer to line 46) with the following results:

1. **Trip_Price and Trip_Distance_km (0.83):**  
   - Strong positive correlation. As trip distance increases, the price tends to increase. This aligns with the expectation that longer trips cost more.

2. **Trip_Price and Trip_Duration_Minutes (0.22):**  
   - Weak positive correlation. Longer durations slightly increase prices, but the relationship is not as strong as with distance.

3. **Traffic_Conditions and Trip_Price (0.06):**  
   - Very weak positive correlation. Traffic conditions have a minimal effect on trip prices, possibly indicating that traffic surcharges or delays play a small role.

4. **Weather and Trip_Price (0.04):**  
   - Very weak positive correlation. Weather has minimal influence on pricing, suggesting adverse weather does not significantly alter prices.

**Other Relationships:**  
Most other features have near-zero correlations with each other, indicating no strong linear relationships.

---

## Machine Learning Methodology 📊🌐🚀

**Algorithm Used:** Linear Regression  

Based on the heatmap, a strong positive correlation exists between **Trip_Distance_km** and **Trip_Price (0.83).** This suggests a linear relationship, making linear regression a suitable choice for predicting trip prices. Linear regression is simple to implement and provides easily interpretable results.

**Model Training:**  
The model used 80% of the data for training and 20% for testing. After training, the model achieved an accuracy of **79%,** providing good predictions compared to actual values.

---

## Results and Discussion 🌟🔢🔎

Results are marked up on ['The_Model'](The_Model.ipynb).

---

## New Improvements 🌐🚀🔧

The model has been integrated with an API and a backend server using **Postman** (https://www.https://www.postman.com/) software. This allows for a user input system via a frontend site, enhancing usability.

---

## References 🔍📑🌐

Kaggle Dataset: [Taxi Trip Pricing](https://www.kaggle.com/datasets/denkuznetz/taxi-price-prediction)


## Starting the Server and The FrontEnd

- To start the Server , Run the [`server.py`](server.py)
- To start the FrontEnd , Run the following Commands : 

```
cd frontend
```

```
cd .\vite-project\
```

```
npm run dev
```

- Follow the Given link after ruuning the Commands 
