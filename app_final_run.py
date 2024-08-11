import streamlit as st
import pandas as pd
import numpy as np
import pickle

clf = pickle.load(open("case_study_university.pkl", "rb"))

def predict(data):
    return clf.predict(data)

st.title("Case Study On University Admission Prediction")
st.markdown("Let's Predict Admission Chances")

col1, col2 = st.columns(2)

with col1:
    GRE = st.slider("GRE Score", 0.0, 340.0, 0.5)
    TOEFL = st.slider("TOEFL Score", 0.0, 120.0, 0.5)
    University = st.slider("University Rating", 1.0, 5.0, 1.0)
    SOP = st.slider("SOP", 1.0, 5.0, 0.5)
    LOR = st.slider("LOR", 1.0, 5.0, 0.5)
    CGPA = st.slider("CGPA", 0.0, 10.0, 0.5)
    Research = st.slider("Research (0 for No, 1 for Yes)", 0, 1, 0)

st.text('')

if st.button("University Admission Prediction"):
    result = predict(np.array([[GRE, TOEFL, University, SOP, LOR, CGPA, Research]]))
    st.text(f"Prediction: {'Admitted' if result[0] == 1 else 'Not Admitted'}")

st.markdown("Developed by Sagar")
