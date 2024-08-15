import streamlit as st
import pandas as pd
import pickle

degrees = pd.read_csv('./data/degrees-that-pay-back.csv')
colleges = pd.read_csv('./data/salaries-by-college-type.csv')
regions = pd.read_csv('./data/salaries-by-region.csv')

# Define the available options for school name, region, and type of school
school_names = colleges['School Name'].unique()
regions = regions['Region'].unique()
school_types = colleges['School Type'].unique()

# Create the Streamlit interface
st.title("School Selection")
st.subheader("Choose the preferred options!")

# Dropdown for selecting school name
selected_school_name = st.selectbox("Select School Name", school_names)

# Dropdown for selecting region
selected_region = st.selectbox("Select Region", regions)

# Dropdown for selecting type of school
selected_school_type = st.selectbox("Select Type of School", school_types)

# Load the linear_model.pkl file
with open('linear_model.pkl', 'rb') as file:
    linear_model = pickle.load(file)

# Create a button for prediction
if st.button("Predict"):
    # Perform prediction using the selected options
    prediction = linear_model.predict([[selected_school_name, selected_region, selected_school_type]])
    # Display the predicted value
    st.write("Predicted Payback is: $ {prediction}")

