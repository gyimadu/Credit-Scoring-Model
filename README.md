# Credit Scoring Model

This project is a Flask web application that uses a machine learning model to predict credit scores based on user input data.

## Features

- **Credit Scoring Prediction**: Enter relevant financial data to get a prediction of the credit score.
- **Machine Learning**: The model was trained using a dataset containing historical credit data.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Credit-Scoring-Model.git
   cd Credit-Scoring-Model

2. Create and activate a virtual environment

    python -m venv credit_scoring_env
    credit_scoring_env\Scripts\activate # On Windows
    source credit_scredit_scoring_env/bin/activate

3. Install required packages

    pip install -r requirements.txt

4. Run the Flask application

    python app.py

5. Open your browser and navigate to

    https://127.0.0.1:5000/

## Usage

1. Home Page: The home page will display a welcome message.

2. Predict Route: Use the `/predict` route to get credit score predictions. You can use Postman or `curl` to send a POST request with the following JSON structure:

    {
        "LIMIT_BAL": 20000,
        "SEX": 2,
        "EDUCATION": 2,
        "MARRIAGE": 2,
        "AGE": 30,
        "PAY_0": -1,
        "PAY_2": 2,
        "PAY_3": 0,
        "PAY_4": 0,
        "PAY_5": 0,
        "PAY_6": 0,
        "BILL_AMT1": 2000,
        "BILL_AMT2": 2000,
        "BILL_AMT3": 2000,
        "BILL_AMT4": 2000,
        "BILL_AMT5": 2000,
        "BILL_AMT6": 2000,
        "PAY_AMT1": 0,
        "PAY_AMT2": 0,
        "PAY_AMT3": 0,
        "PAY_AMT4": 0,
        "PAY_AMT5": 0,
        "PAY_AMT6": 0
    }

3. Response: The model will return a prediction in JSON format

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.
