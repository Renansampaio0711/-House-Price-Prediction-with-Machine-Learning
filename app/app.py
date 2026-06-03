import streamlit as st
import pandas as pd
import joblib
import numpy as np


# Load trained model
model = joblib.load("models/house_price_model.pkl")


st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠"
)


st.title("🏠 House Price Prediction")
st.write("Fill the information below to estimate the house sale price.")


# Numerical features

OverallQual = st.slider(
    "Overall Quality",
    min_value=1,
    max_value=10,
    value=5
)

GrLivArea = st.number_input(
    "Living Area (sq ft)",
    min_value=300,
    max_value=6000,
    value=1500
)

GarageCars = st.number_input(
    "Garage Capacity",
    min_value=0,
    max_value=5,
    value=2
)

TotalBsmtSF = st.number_input(
    "Basement Area (sq ft)",
    min_value=0,
    value=800
)

FullBath = st.number_input(
    "Full Bathrooms",
    min_value=0,
    max_value=5,
    value=2
)

YearBuilt = st.number_input(
    "Year Built",
    min_value=1800,
    max_value=2026,
    value=2000
)

YearRemodAdd = st.number_input(
    "Year Remodeled",
    min_value=1800,
    max_value=2026,
    value=2000
)

LotArea = st.number_input(
    "Lot Area (sq ft)",
    min_value=500,
    value=8000
)

BedroomAbvGr = st.number_input(
    "Bedrooms",
    min_value=0,
    max_value=10,
    value=3
)

KitchenAbvGr = st.number_input(
    "Kitchen Count",
    min_value=1,
    max_value=5,
    value=1
)


# Categorical features

Neighborhood = st.selectbox(
    "Neighborhood",
    [
        'Somerst','ClearCr','IDOTRR','NWAmes','BrDale',
        'SWISU','Sawyer','NAmes','NridgHt','SawyerW',
        'OldTown','BrkSide','CollgCr','Edwards',
        'Gilbert','NPkVill','Crawfor','NoRidge',
        'Blmngtn','Timber','Mitchel','StoneBr',
        'MeadowV','Veenker'
    ]
)


SaleCondition = st.selectbox(
    "Sale Condition",
    [
        "Normal",
        "Abnorml",
        "Partial"
    ]
)


MSZoning = st.selectbox(
    "MS Zoning",
    [
        "RL",
        "RM",
        "FV",
        "RH"
    ]
)


LotShape = st.selectbox(
    "Lot Shape",
    [
        "Reg",
        "IR1",
        "IR2",
        "IR3"
    ]
)



# Create dataframe with same columns used during training

if st.button("Calculate Price"):

    input_data = pd.DataFrame({

        "OverallQual":[OverallQual],
        "GrLivArea":[GrLivArea],
        "GarageCars":[GarageCars],
        "TotalBsmtSF":[TotalBsmtSF],
        "FullBath":[FullBath],
        "YearBuilt":[YearBuilt],
        "YearRemodAdd":[YearRemodAdd],
        "Neighborhood":[Neighborhood],
        "SaleCondition":[SaleCondition],
        "MSZoning":[MSZoning],
        "LotShape":[LotShape],
        "LotArea":[LotArea],
        "BedroomAbvGr":[BedroomAbvGr],
        "KitchenAbvGr":[KitchenAbvGr]

    })
    prediction_log = model.predict(input_data)

    prediction = np.exp(prediction_log)
    st.success(f"Estimated Sale Price: ${prediction[0]:,.2f}")




   

