import requests

url_income = "http://127.0.0.1:5000/predict_income"
url_repayment = "http://127.0.0.1:5000/predict_repayment"

sample_input = {
    "mobile_recharge_avg": 120,
    "recharge_frequency": 2,
    "gps_unique_places": 3,
    "max_daily_distance_km": 5,
    "upi_monthly_volume": 1000,
    "merchant_to_personal_ratio": 0.1,
    "business_app_usage_hours": 0.5,
    "upi_apps_installed": 1,
    "device_price_tier": "low",
    "electricity_bill_punctuality": 0
}


# Test income prediction
res_income = requests.post(url_income, json=sample_input)
print("Income Status Code:", res_income.status_code)
print("Income Raw Response:", res_income.text)

# Test repayment prediction
res_payment = requests.post(url_repayment, json=sample_input)
print("Repayment Status Code:", res_payment.status_code)
print("Repayment Raw Response:", res_payment.text)
