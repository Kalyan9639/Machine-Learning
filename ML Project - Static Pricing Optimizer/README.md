# 📈 Static Price Optimization using Machine Learning

## Overview

This project implements a **Static Price Optimization system** using Machine Learning to help businesses make **better pricing decisions** by understanding how price and related factors influence demand and profit.

Unlike dynamic or reinforcement-learning-based pricing systems, this project focuses on **static decision modeling**:
> _Given historical data, how does demand respond to price changes, and which price is better among multiple options?_

The goal is **decision support**, not automated price control.

---

## Problem Statement

Businesses often struggle to answer questions like:
- How sensitive is customer demand to price changes?
- Will increasing price actually increase profit?
- Which factors truly influence demand?
- Can a model generalize beyond one dataset?

This project answers:
> **“Among possible prices, which one is better for the business under current conditions?”**

---

## Project Scope (What This Project Does)

✅ Learns demand behavior from historical data  
✅ Estimates demand response to price changes  
✅ Simulates pricing scenarios (e.g., +10%, +50%)  
✅ Compares profit before vs after price changes  
✅ Identifies **most influential features**  
✅ Validates behavior under distribution shifts  

❌ Does NOT perform real-time or dynamic pricing  
❌ Does NOT guarantee profit increase for every price rise  
❌ Does NOT replace human decision-making  

---

## Dataset Description

The project uses **industry-inspired synthetic datasets** designed to mimic real-world pricing behavior.

Key input features include:
- `Price`
- `Competitor Price`
- `Discount`
- `Elasticity Index`
- `Storage Cost`
- `Return Rate (%)`
- `Customer Reviews`

Target variable:
- `Demand / Sales Volume`

> ⚠️ Note: The dataset is synthetic but **behaviorally realistic**, designed for learning pricing decision modeling rather than perfect prediction.

---

## Modeling Approach

### 1. Demand Forecasting Model
- Model: **Random Forest Regressor**
- Objective: Predict demand based on pricing and contextual features
- Reason: Non-linear modeling + feature interaction handling

---

### 2. Feature Importance Analysis

The trained model clearly shows:
- **Price** as the dominant factor
- **Elasticity Index** as the second most influential feature
- Other features play secondary but stabilizing roles

This confirms the dataset and model are aligned with real-world pricing theory.

---

### 3. Scenario Simulation

The model is used to simulate pricing decisions:
- Baseline price vs increased price
- Demand change estimation
- Profit comparison

Example:
```python
Price_new = Price * 1.10
```
Demand Ratio:
```
demand_ratio = demand_new / (demand_base + 1e-6)
```
This allows **what-if** analysis without retraining the model.

---

## 4. Profit Comparison Logic

Profit is computed using a simple and interpretable formulation:
```
Profit = Price x Demand
```

For each pricing scenario:
- **Baseline Profit** is calculated using the original price and observed demand
- **New Profit** is calculated using the modified price and the demand predicted by the model

The comparison between baseline and new profit allows the system to evaluate whether a price change is beneficial or harmful.

> Important: A higher price does **not** always lead to higher profit due to demand elasticity effects.

---

## 5. Demand Gap Analysis (Actual vs Predicted)

A demand gap analysis is performed to compare:
- Actual demand from the dataset
- Demand predicted by the trained model

This analysis helps validate:
- Directional correctness of predictions
- Presence of under- or over-estimation
- Stability of the model under distribution shifts

Expected behavior:
- Predicted demand follows the overall trend of actual demand
- Some deviation in magnitude is acceptable
- No extreme spikes or sign reversals should appear

This confirms the model is suitable for **decision support**, even if exact prediction is imperfect.

---

## 6. Validation and Robustness

The model is:
- Trained on one dataset
- Validated on newly generated synthetic data with different distributions

Observed behavior:
- Correct demand direction under price changes
- Reduced accuracy under distribution shift (expected behavior)
- Stable pricing decision outcomes

This mirrors real-world conditions where future data rarely matches training data exactly.

---

## 7. Key Insights

- Price is the dominant driver of demand
- Elasticity Index determines risk associated with price increases
- Profit optimization is not the same as revenue maximization
- Directional correctness is more important than exact prediction
- Static pricing models are effective decision-support tools

---

## 8. Project Structure

├── model_training_on_new_variety_data.ipynb
├── model_validate.ipynb
├── requirements.txt
├── Feature Importance.png
├── output.png
└── README.md


---

## 9. Installation

Install all dependencies using:

```bash
pip install -r requirements.txt
```
#### Requirements

- Python 3.8+
- numpy
- pandas
- matplotlib
- seaborn
- plotly
- scikit-learn
- xgboost

---

## 10. How to Use

1. Open and run `model_training_on_new_variety_data.ipynb`
2. Train the demand forecasting model
3. Analyze feature importance to understand demand drivers
4. Simulate pricing scenarios by modifying the price variable
5. Compare baseline profit vs new profit
6. Run `model_validate.ipynb` to validate model behavior on new data
7. Use the results as pricing decision support

---

## 11. Limitations

- This is a static pricing model (no time-based dynamics)
- Dataset is synthetic and industry-inspired
- Assumes historical demand behavior reflects future patterns
- Not designed for real-time or automated pricing engines
- Predictions may lose magnitude accuracy under distribution shifts

---

## 12. Future Improvements

- Add dynamic pricing using time-series models
- Introduce reinforcement learning for sequential pricing decisions
- Apply causal inference to estimate true price impact
- Add confidence intervals for demand and profit estimates
- Deploy as a pricing decision API or dashboard

---

## 13. Conclusion

This project presents a practical and realistic implementation of a **static price optimization system** using machine learning.

The focus is on:
- Decision modeling instead of automation
- Economic interpretability over raw prediction accuracy
- Robustness under changing data distributions

It provides a strong foundation for building advanced, real-world pricing optimization systems.

---

## Author

**Kalyan**  
AI / Machine Learning Engineer  
Focus: Static Pricing Optimization, Decision Modeling, Applied Machine Learning

---

⭐ If you find this project useful, consider starring the repository.

