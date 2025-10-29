from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return "🏥 Patient Readmission Risk Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Example input: {"features": [65, 1, 120, 85, 98, 0, 1]}
    features = np.array(data["features"]).reshape(1, -1)
    
    # Simple logic for demonstration
    risk_score = np.mean(features)
    risk_label = "High Risk" if risk_score > 50 else "Low Risk"
    
    return jsonify({"readmission_risk": risk_label, "risk_score": float(risk_score)})

if __name__ == '__main__':
    app.run(debug=True)
