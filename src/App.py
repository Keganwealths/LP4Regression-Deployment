# Import necessary libraries
import pandas as pd
import numpy as np
import streamlit as st
import time
import pickle
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: #E2E5DE;
        color: #435763;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
# Insert headers and image
st.title("Sales Prediction")
st.subheader("To help you know your future sales 📈...")
st.image("src/images/Sandiego.jpg")
# Load your dataset
data = pd.read_csv('train.csv') 

# Create a Streamlit app
st.subheader('Dataset Preview')

# Add a button to toggle data visibility
if st.button('Toggle Data Preview'):
    if st.checkbox('Show Preview', value=True):
        st.write(data.head(5))  # Display the top 5 rows of the dataset
    else:
        st.write('Data preview hidden. Click the button to show it again.')

Disp_results = pd.DataFrame()  # Initialize for download

# Create a function to convert the results DataFrame to CSV
def convert_to_csv(df):
    return df.to_csv()

# Taking input from the user
with st.form("This form", clear_on_submit=True):
    st.subheader("Enter the number of day(s)/week(s) you want to predict, And the frequency as D for Daily or W for weekly")
    frequency = str(st.text_input("Frequency 'D' for Daily 'W' for weekly ")).upper()
    Number_of_days = int(st.number_input("Number of day(s)/week(s)"))
    store_nbr = int(st.number_input("Store Number"))
    family = st.text_input("Family")
    onpromotion = st.checkbox("On Promotion")
    price = st.number_input("Price")
    city = st.text_input("City")
    state = st.text_input("State")
    type_x = st.text_input("Type X")
    cluster = st.number_input("Cluster")
    locale = st.selectbox("Locale", ['0', '1'])
    transferred = st.checkbox("Transferred")
    type_y = st.selectbox("Type Y", ['0', '1'])

    submit = st.form_submit_button("Predict your sales")

if submit:
    # Check if the inputs are valid
    if frequency not in ('D', 'W') or Number_of_days <= 0:
        st.error("Please enter a valid frequency ('D' or 'W') and a positive number of days.")
    else:
        # Success message
        st.success("Inputs received successfully ✅")

        try:
            # Generate dummy random data for demonstration purposes
            date_range = pd.date_range(start=pd.Timestamp.today(), periods=Number_of_days, freq=frequency)
            np.random.seed(0)
            random_sales = np.random.randint(50, 200, size=Number_of_days)
            random_lower = random_sales - np.random.randint(10, 30, size=Number_of_days)
            random_upper = random_sales + np.random.randint(10, 30, size=Number_of_days)

            # Create a DataFrame with the dummy data
            dummy_data = pd.DataFrame({
                'Date': date_range,
                'Store Number': [store_nbr] * Number_of_days,
                'Family': [family] * Number_of_days,
                'On Promotion': [onpromotion] * Number_of_days,
                'Price': [price] * Number_of_days,
                'City': [city] * Number_of_days,
                'State': [state] * Number_of_days,
                'Type X': [type_x] * Number_of_days,
                'Cluster': [cluster] * Number_of_days,
                'Type Y': [type_y] * Number_of_days,
                'Locale': [locale] * Number_of_days,
                'Transferred': [transferred] * Number_of_days,
                'Lowest Expected Sales': random_lower,
                'Highest Expected Sales': random_upper,
                'Expected Sales': random_sales
            })

            # Display the predicted sales data
            st.write(f"These are your predicted sales in the next {Number_of_days} {frequency}")
            st.dataframe(dummy_data)

            # Display a line chart of predicted sales
            st.title(f"Line Graph Of Predicted Sales Over {Number_of_days} {frequency}")
            st.line_chart(data=dummy_data.set_index('Date'), use_container_width=True)

            # Create an expander for downloading results as CSV
            expand = st.expander('Download Results as CSV')
            with expand:
                st.download_button(
                    'Download results',
                    convert_to_csv(dummy_data),
                    'prediction_results.csv',
                    'text/csv',
                    'download'
                )

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
