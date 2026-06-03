# 🏠 House Price Prediction with Machine Learning

## 📌 Project Overview

This project aims to develop a Machine Learning model capable of predicting house prices based on property characteristics.

The project includes an exploratory data analysis, data preprocessing, feature engineering, model comparison, and optimization to build a predictive solution.

A Streamlit application was also developed, allowing users to input house features and receive an estimated price prediction through an interactive interface.

---

## 🎯 Project Goals

- Perform Exploratory Data Analysis (EDA)
- Identify patterns and relationships between variables
- Handle missing values and outliers
- Apply feature engineering techniques
- Compare different Machine Learning models
- Optimize the selected model
- Build an interactive prediction application

---

## 📊 Dataset

The dataset contains information about residential properties and their characteristics.

Some of the main features include:

- Living area
- Number of bedrooms
- Number of bathrooms
- Overall quality
- Year built
- Garage area
- Neighborhood
- House price

The target variable is: SalePrice

## 🔎 Exploratory Data Analysis

During the analysis, the following aspects were investigated:

- Distribution of house prices
- Correlation between numerical variables
- Relationship between features and prices
- Missing values
- Outliers

A logarithmic transformation was applied to the target variable to reduce skewness:

```python
log(SalePrice)
```
## ⚙️ Data Preprocessing
The following preprocessing steps were performed:

* Missing value treatment
* Categorical variable encoding
* Feature transformation
* Train/test split
* Target variable transformation
* Data scaling when necessary

## 🤖 Machine Learning Models
Several models were tested and compared:

* Linear Regression
* Ridge Regression
* Lasso Regression
* Elastic Net
* XGBoost

The models were evaluated using cross-validation and the RMSE metric.

The final selected model was:

## 🏆 Lasso Regression

Lasso was chosen due to its balance between:

Prediction performance
Model simplicity
Generalization ability

## 📈 Model Evaluation
The evaluation metric used was RMSE.Lower RMSE values indicate better prediction accuracy.


## 🖥️ Application

A web application was created using Streamlit.

Users can enter house characteristics and receive a predicted price.


## 🛠️ Technologies Used
* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* Streamlit
* Joblib

## ▶️ How to Run the Project
Clone the repository:
``` bash
git clone https://github.com/your_username/house-prediction.git
```
Install dependencies:
``` bash
pip install -r requirements.txt
```
Run the Streamlit application:
``` bash
streamlit run app/app.py
``` 

## 👤 Author

Renan Sampaio

Machine Learning project developed to apply Data Analysis and predictive modeling techniques.