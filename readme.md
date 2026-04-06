# Singapore HDB Resale Price Predictor

A machine learning web application that predicts Singapore HDB (Housing Development Board) resale flat prices based on historical transaction data.

🔗 **Live App:** https://singapore-housing-cnfcnm8fbrnomkn7prjnch.streamlit.app/

---

## What It Does

Users input flat details — town, flat type, floor level, area, lease information — and the app predicts the estimated resale price using a trained Random Forest model.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| ML Model | Random Forest Regressor (scikit-learn) |
| Data Processing | Pandas, NumPy |
| Feature Engineering | Label Encoding, Regex parsing |

---

## Model Performance

| Metric | Score |
|---|---|
| R² Score | 0.9587 |
| MAE | SGD 26,207 |
| RMSE | SGD 38,327 |

The model explains **95.87%** of price variation in the test set.

---

## Features Used

- Town (26 unique areas)
- Flat Type (1-5 rooms, Executive, Multi-Generation)
- Flat Model
- Storey Range (converted to average floor level)
- Floor Area (sqm)
- Lease Commence Date
- Remaining Lease (years, parsed from text)
- Transaction Year

---

## Data Source

Singapore Housing Development Board (HDB) resale flat transactions from Jan 2017 onwards, sourced from [data.gov.sg](https://data.gov.sg/collections/189/view).

228,225 transaction records used for training and evaluation.

---

## Project Structure

```
singapore-housing/
├── app.py                          # Streamlit application
├── singapore_functions.py          # Data processing + model training + prediction
├── ResaleflatpricesbasedonregistrationdatefromJan2017onwards.csv
├── requirements.txt
└── README.md
```

---

## How to Run Locally

1. Clone the repo:
```
git clone https://github.com/akashravuru/singapore-housing
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the app:
```
streamlit run app.py
```

Note: Model trains on first load (~1-2 minutes). Subsequent predictions are instant.

---

Built by [Akash Ravuru](https://linkedin.com/in/akashravuru)