from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# load trained model
model = joblib.load('credit_scoring_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return 'Welcome to the Credit Scoring App!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([data['features']])
    features_scaled = scaler.tramsform(features)
    prediction = model.predict(features_scaled)
    return jsonify({'default': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)

joblib.dump(model, 'credit_scoring_model.pkl')
joblib.dump(scaler, 'scaler.pkl')