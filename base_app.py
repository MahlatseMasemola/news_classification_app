import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load your raw data
raw_data_path = 'cleaned_test.csv'
raw_data = pd.read_csv(raw_data_path)

# Load your pickled models
models = {
    "Logistic Regression": "Logistic_Regression_best_model.pkl",
    "Multinomial Naive Bayes": "Multinomial_Naive_Bayes_best_model.pkl",
    "SVM": "SVM_best_model.pkl"
}

# Load vectorizer
vectorizer_path = "vectorizer.pkl"
with open(vectorizer_path, 'rb') as file:
    vectorizer = pickle.load(file)

def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Main function for the Streamlit web app
def main():
    st.title("News Classifier")
    st.subheader("Analyzing news articles")

    options = ["Home", "Prediction", "Information", "Insights"]
    selection = st.sidebar.selectbox("Choose Option", options)
    
    if selection == "Home":
        st.info("Welcome to the News Classifier App")
        st.markdown("Use this application to classify news articles using different machine learning models.")
        
        st.subheader("Dataset Overview")
        st.dataframe(raw_data.head())

    if selection == "Information":
        st.info("General Information")
        st.markdown("Some information here")

    if selection == "Prediction":
        st.info("Prediction with ML Models")
        news_text = st.text_area("Enter Text", "Type Here")

        model_choice = st.sidebar.selectbox("Choose Machine Learning Model", list(models.keys()))

        if st.button("Classify"):
            vect_text = vectorizer.transform([news_text]).toarray()

            model_path = models[model_choice]
            model = load_model(model_path)

            prediction = model.predict(vect_text)

            mapping = {0: 'business', 1: 'education', 2: 'entertainment', 3: 'sports', 4: 'technology'}
            category = mapping.get(prediction[0], "Unknown")

            st.success(f"Text Categorized as: {category}")

    elif selection == "Insights":
        st.info("Insights about the Models")

        performance_metrics = {
            "Logistic Regression": 0.9819,
            "Multinomial Naive Bayes": 0.978,
            "SVM": 0.9745
        }

        st.markdown("### Model Performance Comparison")
        st.markdown("""
        The performance of different machine learning models used in this application is as follows:

        - **Logistic Regression:** 98.19%
        - **Multinomial Naive Bayes:** 97.80%
        - **SVM:** 97.45%
        
        """)
        st.write("This section compares the performance of different machine learning models used in this application.")

        if st.button("Compare Models"):
            fig, ax = plt.subplots()
            models_names = list(performance_metrics.keys())
            accuracies = list(performance_metrics.values())
            
            colors = sns.color_palette("hsv", len(models_names))
            ax.barh(models_names, accuracies, color=colors)
            ax.set_xlabel('Accuracy')
            ax.set_title('Model Comparison')

            st.pyplot(fig)

if __name__ == '__main__':
    main()
