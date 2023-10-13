# Building Machine Learning Applications with Streamlit
This Streamlit App allows you to predict future sales using the Prophet model. It provides an interface to input the number of days or weeks you want to predict and the frequency of predictions. The app uses the trained Prophet model to generate sales predictions and displays them along with a line graph of the predicted sales.
## Installation
To run this app locally, you need to follow these steps:

1. Clone the repository:
   ```shell
   git clone <repository_url>
(i) Install the required dependencies:
     pip install -r requirements.txt
(ii) Run the Streamlit app:
     streamlit run app.py

## Usage
1. Open the app in your web browser. You should see a welcome message and an image related to sales prediction.

2. Enter the number of days or weeks you want to predict and select the frequency (daily or weekly) for the predictions.

3. Click the "Predict your sales" button to initiate the prediction process.

4. Once the predictions are generated, the app displays the predicted sales data in a table. If the frequency is set to weekly, the output will be displayed in weeks; otherwise, it will be displayed in days.

5. Additionally, a line graph of the predicted sales over the specified period is shown.

6. You can download the predicted sales results as a CSV file by clicking the "Download results" button in the "Download Results as CSV" section.

7. In the sidebar, there are two options: "About" and "About the sales prediction". Clicking on each option will display additional information about the app and the sales prediction problem.

## File Structure
The main files and directories in this repository are organized as follows:

- app.py: The main Streamlit app file that contains the code for the sales prediction app.
- src/model/prophet_model.pkl: The serialized Prophet model used for making predictions.
- src/images/future.PNG: An image related to sales prediction displayed in the app.

## About
This Sales Prediction app was developed as part of the Azubi Africa Data Analysis Training program. It uses the Prophet model, a time series forecasting algorithm, to predict future sales for Corporation Favorita, a large Ecuadorian-based grocery retailer.

For more information about the app or the sales prediction problem, please refer to the documentation or contact the app administrator.

## License
   This project is licensed under the MIT License.

## Author
Kevin Kegan Olome (Team San Diego)