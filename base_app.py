{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54dc0fa7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import pickle\n",
    "\n",
    "# Load the models and vectorizer\n",
    "with open('Multinomial Naive Bayes_best_model.pkl', 'rb') as file:\n",
    "    nb_model = pickle.load(file)\n",
    "with open('SVM_best_model.pkl', 'rb') as file:\n",
    "    svm_model = pickle.load(file)\n",
    "with open('Logistic Regression_best_model.pkl', 'rb') as file:\n",
    "    lr_model = pickle.load(file)\n",
    "with open('vectorizer.pkl', 'rb') as file:\n",
    "    vectorizer = pickle.load(file)\n",
    "\n",
    "# Title\n",
    "st.title('Newspaper Classification App')\n",
    "\n",
    "# User input\n",
    "user_input = st.text_area(\"Enter the text for classification\")\n",
    "\n",
    "# Predict\n",
    "if st.button(\"Classify\"):\n",
    "    if user_input:\n",
    "        # Vectorize the input\n",
    "        user_input_vect = vectorizer.transform([user_input])\n",
    "        \n",
    "        # Get predictions\n",
    "        nb_pred = nb_model.predict(user_input_vect)\n",
    "        svm_pred = svm_model.predict(user_input_vect)\n",
    "        lr_pred = lr_model.predict(user_input_vect)\n",
    "        \n",
    "        # Display predictions\n",
    "        st.write(f\"Multinomial Naive Bayes Prediction: {nb_pred[0]}\")\n",
    "        st.write(f\"SVM Prediction: {svm_pred[0]}\")\n",
    "        st.write(f\"Logistic Regression Prediction: {lr_pred[0]}\")\n",
    "    else:\n",
    "        st.write(\"Please enter text for classification.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
