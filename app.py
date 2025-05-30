from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Step 1:
def generate_synthetic_data(n=100):
    np.random.seed(42)
    data = pd.DataFrame({
        'mobile_recharge_avg': np.random.uniform(100, 1000, n),
        'recharge_frequency': np.random.randint(1, 10, n),
        'gps_unique_places': np.random.randint(1, 20, n),
        'max_daily_distance_km': np.random.uniform(1, 50, n),
        'upi_monthly_volume': np.random.uniform(1000, 50000, n),
        'merchant_to_personal_ratio': np.random.uniform(0, 1, n),
        'business_app_usage_hours': np.random.uniform(0, 10, n),
        'upi_apps_installed': np.random.randint(1, 5, n),
        'device_price_tier': np.random.choice(['low','mid','high'], n),
        'electricity_bill_punctuality': np.random.choice([0,1], n)
    })

    # Encode device_price_tier
    le = LabelEncoder()
    data['device_price_tier_enc'] = le.fit_transform(data['device_price_tier'])

    # Target: Monthly income (in INR) 
    data['income'] = (
        data['mobile_recharge_avg'] * 10 +
        data['recharge_frequency'] * 0.3 + 
        data['business_app_usage_hours'] * 500 +
        data['electricity_bill_punctuality'] * 2000 + 
        data['device_price_tier_enc'] * 1000 + 
        np.random.normal(0, 5000, n)
    ).clip(lower=1000) # minimum income 1000

    # Target: repayment capability (binary)
    data['repayment'] = ((data['income'] > 15000) | (data['electricity_bill_punctuality'] == 1)).astype(int)

    return data, le


# Generate data and label encoder
data, le_device = generate_synthetic_data()

repayment_counts = data['repayment'].value_counts()
print("Repayment Class Distribution:")
print(repayment_counts)

# Features and targets
feature_cols = [
    'mobile_recharge_avg', 'recharge_frequency', 'gps_unique_places', 'max_daily_distance_km', 'upi_monthly_volume', 'merchant_to_personal_ratio', 'business_app_usage_hours', 'upi_apps_installed', 'device_price_tier_enc', 'electricity_bill_punctuality'
]
X = data[feature_cols]
y_income = data['income']
y_repayment = data['repayment']

# Step 2: Train models
income_model = RandomForestRegressor(n_estimators=100, random_state=42)
income_model.fit(X,y_income)

repayment_model = LogisticRegression(class_weight='balanced')
repayment_model.fit(X, y_repayment)

# Step 3: Define helper to preprocess input JSON
def preprocess_input(json_data):
    try:
        device_tier = json_data.get('device_price_tier','low').lower()
        device_tier_enc = le_device.transform([device_tier])[0] if device_tier in le_device.classes_ else 0

        input_features = [
            float(json_data.get('mobile_recharge_avg', 0)),
            int(json_data.get('recharge_frequency', 0)),
            int(json_data.get('gps_unique_places', 0)),
            float(json_data.get('max_daily_distance_km', 0)),
            float(json_data.get('upi_monthly_volume', 0)),
            float(json_data.get('merchant_to_personal_ratio', 0)),
            float(json_data.get('business_app_usage_hours', 0)),
            int(json_data.get('upi_apps_installed', 0)),
            int(json_data.get('electricity_bill_punctuality', 0)),
            int(device_tier_enc)  
        ]

        return np.array(input_features).reshape(1,-1)
    except Exception as e:
        return None
    
# Step 4: API Endpoints

@app.route('/predict_income', methods=['POST'])
def predict_income():
    json_data = request.json
    features = preprocess_input(json_data)
    if features is None:
        return jsonify({'error':'Invalid input data'}), 400
    income_pred = income_model.predict(features)[0]
    return jsonify({'predicted_income': round(income_pred, 2)})

@app.route('/predict_repayment', methods=['POST'])
def predict_repayment():
    json_data = request.json
    features = preprocess_input(json_data)
    if features is None:
        return jsonify({'error': 'Invalid input data'}), 400
    repayment_prob = repayment_model.predict_proba(features)[0][1]
    repayment_pred = int(repayment_prob > 0.5)
    return jsonify({'predicted_repayment_capability': repayment_pred,'repayment_probability':round(repayment_prob, 2)})

if __name__ == '__main__':
    app.run(debug=True)