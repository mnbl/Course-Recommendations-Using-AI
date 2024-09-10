
# AI-Powered Course Recommendations

This project uses machine learning models to recommend courses based on student data. The project provides both a Jupyter notebook for in-depth analysis and a Streamlit app for real-time recommendations.

## Project Overview

- **Course Recommendation System**: Predicts and recommends courses for students based on their preferences and data.
- **Web App**: A simple interface to allow users to interact with the trained model and get recommendations.

## Features

- **Data Analysis**: The Jupyter notebook provides steps for data exploration and model training.
- **Model Training**: Uses machine learning to generate recommendations based on student profiles.
- **Web Interface**: Users can interact with the recommendation system through a Streamlit application.

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/mnbl/Course-Recommendations-Using-AI
   cd Course-Recommendations-Using-AI
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

### Option 1: Running the Jupyter Notebook

1. Open the notebook:
   ```bash
   jupyter notebook
   ```

2. Run the notebook file `Predict_School.ipynb` to analyze the data and train the recommendation models.

### Option 2: Running the Streamlit App

1. Navigate to the folder containing `streamlit_app.py`.

2. Run the application:
   ```bash
   streamlit run streamlit_app.py
   ```

3. Open your browser and navigate to the URL provided by Streamlit to interact with the recommendation system.

## Dataset

The project uses a dataset:
- `data/course_data.csv`: Contains information about students and their preferences used for training the model.

## Contributions

Feel free to contribute by submitting pull requests or suggesting improvements!
