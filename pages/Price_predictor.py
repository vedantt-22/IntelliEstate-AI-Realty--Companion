import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sidebar import load_sidebar
# sidebar
load_sidebar()
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {display: none;}
    </style>
""", unsafe_allow_html=True)
st.set_page_config(page_title='🏷️ Property Price Predictor', layout='centered')


with open('D:\DOCUMENTS\Projects\IntelliEstate - AI Realty Companion\df (1).pkl','rb') as file:
    df = pickle.load(file)

with open('D:\DOCUMENTS\Projects\IntelliEstate - AI Realty Companion\pipeline (1).pkl','rb') as file:
    pipeline = pickle.load(file)

st.markdown("<h1 style='text-align: center;'>🧮 Property Price Estimator</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: #555;'>Enter property details below to predict the estimated price in crores 💰</p>",
    unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# property_type
property_type = st.selectbox('Property Type',['flat','house'])

# sector
sector = st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

bedrooms = float(st.selectbox('Number of Bedroom',sorted(df['bedRoom'].unique().tolist())))

bathroom = float(st.selectbox('Number of Bathrooms',sorted(df['bathroom'].unique().tolist())))

balcony = st.selectbox('Balconies',sorted(df['balcony'].unique().tolist()))

property_age = st.selectbox('Property Age',sorted(df['agePossession'].unique().tolist()))

built_up_area = float(st.number_input('Built Up Area'))

servant_room = float(st.selectbox('Servant Room',[0.0, 1.0]))
store_room = float(st.selectbox('Store Room',[0.0, 1.0]))

furnishing_type = st.selectbox('Furnishing Type',sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.selectbox('Luxury Category',sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox('Floor Category',sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):

    # form a dataframe
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    #st.dataframe(one_df)

    # Predict price
    try:
        base_price = np.expm1(pipeline.predict(one_df))[0]
        low = round(base_price - 0.22, 2)
        high = round(base_price + 0.22, 2)

        st.success("✅ Prediction Successful!")

        st.markdown(f"""
            <div style='padding: 1rem; background-color: #f1f5f9; border-radius: 10px; border-left: 5px solid #2a9d8f;'>
                <h3 style='color: #2a9d8f;'>💸 Estimated Price Range:</h3>
                <h2 style='color: #000;'>₹ {low} Cr – ₹ {high} Cr</h2>
                <p style='color: #555;'>This estimate is based on the current model trained on Gurgaon real estate data.</p>
            </div>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
