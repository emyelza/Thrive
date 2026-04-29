
# Thrive

Your financial companion for getting through the semester.
Thrive helps university students understand their spending and predict how long their money will last , using nothing more than a bank statement.

Upload a CSV. Get clarity instantly.

# What it does
* Predicts how long your balance will last
* Estimates your run-out date based on real spending
* Categorises transactions automatically
* Highlights risky spending patterns
* Suggests simple, actionable improvements

This is not a budgeting app.
It’s a financial early-warning system.

# How it works

1. Upload your bank statement (CSV).
2. Thrive analyses your recent spending
3. You get:
   * Daily burn rate
   * Days remaining
   * Spending breakdown
   * Behavioural insights

All in a single dashboard.

# Key Features

* Survival Prediction
  Understand how long your money will last based on actual behaviour

* Smart Categorisation
  Automatically groups expenses like food, transport, shopping

* Manual Tagging
  Fix unknown transactions instantly

* Behavioural Insights
  Detect patterns like weekend overspending or frequent small spends

* Actionable Advisory
  Simple suggestions that actually help you stretch your money

* Privacy First
  No login. No storage. Everything runs locally in memory

# Tech Stack

* Python
* Streamlit
* Pandas
* Matplotlib

# Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/thrive.git
cd thrive
pip install -r requirements.txt
streamlit run app.py
```
Open: [http://localhost:8501](http://localhost:8501)

# Input Format

Upload a CSV with:
```
Date, Description, Amount, Type, Balance
```
Works with most Indian bank exports (SBI, HDFC, ICICI, Axis, etc.)
---
# Live Demo

Add your deployed link here after deployment:
```
https://thrive-jmky7j3ohu3vxo5zp4qc72.streamlit.app
```

# Who this is for

University students managing:
* monthly allowance
* part-time income
* UPI-based spending

# Why Thrive

Most people realise they’re out of money after it happens.
Thrive helps you see it before.

# Future Improvements

* ML-based transaction categorisation
* Spending trend predictions
* Goal-based saving insights
* Mobile version

# License
MIT License

# Author

Your Name
GitHub: [https://github.com/YOUR_USERNAME](https://github.com/emyelza)
