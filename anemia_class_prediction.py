#importing modules
import urllib

import pandas as pd
import joblib
import streamlit as st

#loading model and encoder
model = joblib.load("anemia_model.pkl")
ct = joblib.load("anemia_encoder.pkl")

#converting to streamlit
name = "Sadiq Inuwa"
goal = "1.To predicts a particular class of anemia from the provided clinical values. 2.To confirm the legitimates of a test result !"
st.logo("IMG_0029.jpg")
st.sidebar.title("ABOUT US!")
st.sidebar.caption(f"Developer: {name}.")
st.sidebar.title("CONTACTS US...")
st.sidebar.link_button("facebook", 'https://www.facebook.com/sadeeq.alhinuwa')
st.sidebar.link_button("email", 'sadiqinuwa6@gmail.com')
st.sidebar.link_button("WhatsApp", 'https://wa.me/2347067717477')
st.title("ANEMIA CLASS PREDICTION")
st.caption(f"GOAL: {goal}")


#accepting users input
hemoglobin = st.number_input("Please Enter The Evaluated Hemoglobin Value!")
MCV = st.number_input("Please Enter The Evaluated Mean Corpuscular Volume (MCV) Value!")
MCH = st.number_input("Please Enter The Evaluated Mean Corpuscular Hemoglobin (MCH) Value!")
RDW = st.number_input("Please Enter The Evaluated Red Cell Distribution Width(RDW) Value!")
Reticulocyte = st.number_input("Please Enter The Evaluated Reticulocyte Value!")
Serum_Iron = st.number_input("Please Enter The Evaluated Serum_Iron Value!")
Ferritin = st.number_input("Please Enter The Evaluated Ferritin Value!")
Vitamin_B12 = st.number_input("Please Enter The Evaluated Vitamin_B12 Value!")

#forming prediction DataFrame
if st.button("Predict Anemia Class"):
    prediction_data = pd.DataFrame({
        "Hemoglobin": [hemoglobin],
        "MCV": [MCV],
        "MCH": [MCH],
        "RDW": [RDW],
        "Reticulocyte": [Reticulocyte],
        "Serum_Iron": [Serum_Iron],
        "Ferritin": [Ferritin],
        "Vitamin_B12": [Vitamin_B12]
    })

    #transforming the prediction DataFrame
    predicted_data = ct.transform(prediction_data)

    #making prediction
    predictions = model.predict(predicted_data)
    st.success(f"Anemia Class: {predictions[0]} Anemia")




