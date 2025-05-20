# 🧠 Credit Underwriting AI API

This is a lightweight Flask-based API project that predicts a user’s **monthly income** and **repayment capability** using **non-traditional data** — like mobile recharge, UPI usage, app behavior, and more.

🎯 **Built for:** Credit Underwriting Innovation Hackathon  
🚀 **Goal:** Help assess financial reliability of the underserved population using alternative data sources.

---

## 🔍 What It Does

- ✅ **Predicts Monthly Income** using Random Forest Regressor  
- ✅ **Classifies Repayment Capability** using Logistic Regression  
- ✅ Uses behavioral features like:
  - Mobile recharge average  
  - UPI monthly volume  
  - Number of unique places (via GPS)  
  - Business app usage hours  
  - Device price tier  
  - Electricity bill punctuality, and more

---

## 🛠️ Tech Stack

- Python 🐍  
- Flask 🔥  
- scikit-learn 🤖  
- Pandas / NumPy 📊  
- REST APIs using Flask

---

## 📁 Folder Structure

creadit_underwriting/
│
├── app.py # Main Flask API
├── test_api.py # Testing script using requests
├── requirements.txt # All dependencies
├── .gitignore # To avoid committing venv & pycache
└── venv/ # Virtual environment (excluded)

---

## 📡 API Endpoints

### 1. `/predict_income`  
- **Method:** `POST`  
- **Input:** JSON with user behavior  
- **Output:** Predicted monthly income (in INR)

### 2. `/predict_repayment`  
- **Method:** `POST`  
- **Input:** Same JSON  
- **Output:** Repayment capability (0 or 1) and probability

📦 **Sample Input:**
```json
{
  "mobile_recharge_avg": 500,
  "recharge_frequency": 5,
  "gps_unique_places": 10,
  "max_daily_distance_km": 15,
  "upi_monthly_volume": 15000,
  "merchant_to_personal_ratio": 0.3,
  "business_app_usage_hours": 3,
  "upi_apps_installed": 2,
  "device_price_tier": "mid",
  "electricity_bill_punctuality": 1
}


▶️ How to Run
1. Clone the repo
2. Create a virtual environment
3. Install dependencies
4. Run the Flask app

git clone https://github.com/yourusername/creadit_underwriting.git
cd creadit_underwriting
python -m venv venv
venv\Scripts\activate        # for Windows
pip install -r requirements.txt
python app.py

To test API:
python test_api.py

Made with 💖 by @aadyanair