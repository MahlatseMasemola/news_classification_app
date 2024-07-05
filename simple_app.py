#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


# Load models
with open('Logistic Regression_best_model.pkl', 'rb') as f:
    lr_model = pickle.load(f)
with open('Multinomial Naive Bayes_best_model.pkl', 'rb') as f:
    nb_model = pickle.load(f)
with open('SVM_best_model.pkl', 'rb') as f:
    svm_model = pickle.load(f)

# Load vectorizer
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Streamlit app
st.title("Newspaper Categorization")

# User input
user_input = st.text_area("Enter the text for classification")

# Model selection
model_option = st.selectbox("Select the model", ("Logistic Regression", "Multinomial Naive Bayes", "SVM"))

# Classification button
if st.button("Classify"):
    if user_input:
        user_input_vect = vectorizer.transform([user_input])
        
        if model_option == "Logistic Regression":
            prediction = lr_model.predict(user_input_vect)
        elif model_option == "Multinomial Naive Bayes":
            prediction = nb_model.predict(user_input_vect)
        elif model_option == "SVM":
            prediction = svm_model.predict(user_input_vect)
        
        st.write(f"The text is classified as: {prediction[0]}")
    else:
        st.write("Please enter some text for classification.")

