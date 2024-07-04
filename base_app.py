{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "54469f0d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-07-05 00:34:23.119 \n",
      "`st.cache` is deprecated and will be removed soon. Please use one of Streamlit's new caching commands, `st.cache_data` or `st.cache_resource`.\n",
      "More information [in our docs](https://docs.streamlit.io/develop/concepts/architecture/caching).\n",
      "\n",
      "**Note**: The behavior of `st.cache` was updated in Streamlit 1.36 to the new caching logic used by `st.cache_data` and `st.cache_resource`.\n",
      "This might lead to some problems or unexpected behavior in certain edge cases.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import pickle\n",
    "\n",
    "# Function to load the pickled model\n",
    "@st.cache(allow_output_mutation=True)\n",
    "def load_model(model_file):\n",
    "    with open(model_file, 'rb') as file:\n",
    "        model = pickle.load(file)\n",
    "    return model\n",
    "\n",
    "def main():\n",
    "    st.title('Newspaper Article Classifier')\n",
    "    st.sidebar.title('Navigation')\n",
    "    page = st.sidebar.radio('Go to', ('Home', 'Prediction', 'About'))\n",
    "\n",
    "    if page == 'Home':\n",
    "        st.write('This is the home page.')\n",
    "\n",
    "    elif page == 'Prediction':\n",
    "        st.subheader('Make a Prediction')\n",
    "        text = st.text_area('Enter the text of the article:')\n",
    "        model_name = st.selectbox('Select Model', ('Multinomial Naive Bayes', 'SVM', 'Logistic Regression'))\n",
    "        \n",
    "        if st.button('Classify'):\n",
    "            if text.strip() == '':\n",
    "                st.warning('Please enter some text.')\n",
    "            else:\n",
    "                # Load the selected model\n",
    "                if model_name == 'Multinomial Naive Bayes':\n",
    "                    model = load_model('Multinomial Naive Bayes_best_model.pkl')\n",
    "                elif model_name == 'SVM':\n",
    "                    model = load_model('SVM_best_model.pkl')\n",
    "                elif model_name == 'Logistic Regression':\n",
    "                    model = load_model('Logistic Regression_best_model.pkl')\n",
    "\n",
    "                # Perform prediction\n",
    "                prediction = model.predict([text])\n",
    "                prediction_proba = model.predict_proba([text])\n",
    "\n",
    "                # Display results\n",
    "                st.success(f'Predicted Category: {prediction[0]}')\n",
    "                st.info(f'Probability: {prediction_proba.max():.2f}')\n",
    "\n",
    "    elif page == 'About':\n",
    "        st.subheader('About')\n",
    "        st.write('This is a Streamlit web application for classifying newspaper articles.')\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e06342bf",
   "metadata": {},
   "outputs": [],
   "source": []
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
