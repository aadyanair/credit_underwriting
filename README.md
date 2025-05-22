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

## 📡 API Endpoints

### 1. `/predict_income`  
- **Method:** `POST`  
- **Input:** JSON with user behavior  
- **Output:** Predicted monthly income (in INR)

### 2. `/predict_repayment`  
- **Method:** `POST`  
- **Input:** Same JSON  
- **Output:** Repayment capability (0 or 1) and probability



## ▶️ How to Run
1. Clone the repo
2. Create a virtual environment
3. Install dependencies
4. Run the Flask app


Made with 💖 by @aadyanair