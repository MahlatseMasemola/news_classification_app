<div align="center">
    <h1>News Classification App</h1>
    <img src="https://static.vecteezy.com/system/resources/previews/020/621/496/non_2x/sitemap-classification-concept-icon-in-line-style-design-isolated-on-white-background-editable-stroke-free-vector.jpg" alt="News Classification" width="300"/>
</div>

## Introduction

The News Classification App is a machine learning-based web application built using Streamlit. This app classifies news articles into different categories such as Business, Education, Entertainment, Sports, and Technology. It leverages various machine learning models to automate the categorization process, enhancing operational efficiency and user experience for news outlets.

### Use and Benefits

In the digital age, news outlets produce an enormous volume of content daily, making manual categorization both challenging and time-consuming. The News Classification App addresses this challenge by automatically classifying news articles, improving searchability and reader experience. It allows editorial teams to manage content more efficiently and make data-driven decisions. This automation is beneficial for:

- **News Publishers:** Streamlines content management and enhances reader engagement by delivering relevant articles.
- **Editors and Journalists:** Saves time and effort in categorizing articles, allowing them to focus on content creation.
- **Readers:** Enhances the user experience by providing accurately categorized news content.

### How It Works

The app uses pre-trained machine learning models to classify the input text. Users can input news articles into the app, which then processes the text using natural language processing (NLP) techniques and classifies it into one of the predefined categories. The app supports multiple models, including Logistic Regression, SVM, and Multinomial Naive Bayes, providing flexibility and options for classification.

## Table of Contents

1. [Introduction](#introduction)
2. [Key Features](#key-features)
3. [Getting Started](#getting-started)
4. [Usage](#usage)
5. [Packages](#packages)
6. [Environment Setup](#environment-setup)
7. [Contributors](#contributors)

## Key Features

- **Automated News Classification:** Classifies news articles into predefined categories using machine learning models.
- **Multiple Models:** Supports Logistic Regression, SVM, and Multinomial Naive Bayes.
- **Interactive Interface:** User-friendly interface built with Streamlit.
- **Insights and Analytics:** Provides insights and metrics about the classification models.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have the following installed:

- Python 3.9
- Pip

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/MahlatseMasemola/news_classification_app.git
    cd news_classification_app
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run simple_app.py
    ```

## Usage

1. Navigate to the URL provided by Streamlit after running the app (usually `http://localhost:8501`).
2. Use the sidebar to select the model and input the news article text.
3. Click on the "Classify" button to get the classification result.

## Packages

To carry out all the objectives for this repository, the following necessary dependencies need to be loaded:

- `Pandas 2.2.2`
- `Numpy 1.26.4`
- `Matplotlib 3.8.4`
- `Seaborn`
- `Scikit-learn`
- `Streamlit`

## Environment Setup

It is highly recommended to use a virtual environment for projects. Follow these steps to set up your environment:

### Setup - you only need to do this once

```bash
# make sure your pip in your base Python installation is up-to-date
python3 -m pip install -U pip
# install the virtualenv package
python3 -m pip install virtualenv

# create a virtual environment in this directory called '.venv'
python3 -m venv .venv
# you should now see the folder `.venv` in your repo

# activate the virtual environment
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
# install the requirements for this project
pip install -r requirements.txt
```

## Contributors

Thanks to the following people who have contributed to this project:

| Name                                                                                        |  Email              
|-------------------------------------------|-----------------------------------------|
| [Mahlatse Masemola](mailto:masemola.hunadi@gmail.com) (Group Leader)              | masemola.hunadi@gmail.com             |
| [Keamogetswe Mothoa](mailto:keamogetswemitchellmothoa@gmail.com) (Project Manager)| keamogetswemitchellmothoa@gmail.com   |
| [Sene Mpungose](mailto:leebunny1623@gmail.com)                                    | leebunny1623@gmail.com                |
| [Dimpho Leb](mailto:dimpholebea28@gmail.com)                                      | dimpholebea28@gmail.com               |
| [Tikedzani Geraldine V](mailto:geraldinevele@gmail.com)                           | geraldinevele@gmail.com               |
| [Nomkhosi Si](mailto:nomkhosisyamthanda@gmail.com)                                | nomkhosisyamthanda@gmail.com          |
