import streamlit as st
import pandas as pd
import numpy as np
import pickle

clf = pickle.load(open("case_study_university.pkl","rb"))

def predict(data):
    clf = pickle.load(open("case_study_university.pkl","rb"))
    return clf.predict(data)

st.title("Case Study On University Admission Prediction")
st.markdown("Lets Predict Admission chances")

col1,col2 = st.columns(2)

with col1:
    
    GRE = st.sidebar.slider("GRE Score", 1.0, 10000.0, 0.5)
   
    TOEFL  = st.sidebar.slider("TOEFL Score", 1.0, 10000.0, 0.5)
    
    University  = st.sidebar.slider("University Rating", 1.0, 10000.0, 0.5)
 
    SOP = st.sidebar.slider("SOP", 1.0, 10000.0, 0.5)
  
    LOR = st.sidebar.slider("LOR", 1.0, 10000.0, 0.5)
   
    CGPA = st.sidebar.slider("CGPA", 1.0, 10000.0, 0.5)
    
    Research = st.sidebar.slider("Research", 1.0, 10000.0, 0.5)
                          
st.text('')
if st.button("University Admission Prediction"):
    result= clf.predict(np.array([[GRE,TOEFL,University,SOP,LOR,CGPA,Research]]))
    st.text(result[0])
    
st.markdown("Developed by Sagar")
                  
