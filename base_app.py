#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import pickle

# Load the models and vectorizer
with open('Multinomial Naive Bayes_best_model.pkl', 'rb') as file:
    nb_model = pickle.load(file)
with open('SVM_best_model.pkl', 'rb') as file:
    svm_model = pickle.load(file)
with open('Logistic Regression_best_model.pkl', 'rb') as file:
    lr_model = pickle.load(file)
with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Title
st.title('Newspaper Classification App')

# User input
user_input = st.text_area("Enter the text for classification")

# Predict
if st.button("Classify"):
    if user_input:
        # Vectorize the input
        user_input_vect = vectorizer.transform([user_input])
        
        # Get predictions
        nb_pred = nb_model.predict(user_input_vect)
        svm_pred = svm_model.predict(user_input_vect)
        lr_pred = lr_model.predict(user_input_vect)
        
        # Display predictions
        st.write(f"Multinomial Naive Bayes Prediction: {nb_pred[0]}")
        st.write(f"SVM Prediction: {svm_pred[0]}")
        st.write(f"Logistic Regression Prediction: {lr_pred[0]}")
    else:
        st.write("Please enter text for classification.")


# In[ ]:




