# 🏠 House Price Data Science Pipeline

## 🚀 Overview

This project demonstrates a **complete data science pipeline** using statistical analysis and preprocessing techniques to improve machine learning performance.

It focuses on:

* Understanding data distributions
* Detecting and handling outliers
* Fixing skewness
* Feature scaling
* Evaluating impact on model performance

The goal is to move beyond basic modeling and apply **real-world statistical reasoning** used in production data science workflows.

---

## 📊 Dataset

* California Housing Dataset (from `sklearn`)
* Features include:

  * Median income
  * House age
  * Population
  * Location-based metrics

---

## 🧠 Key Concepts Applied

### 1. Central Tendency

* Mean
* Median
* Mode (conceptual)

### 2. Spread

* Standard Deviation

### 3. Distribution Analysis

* Normal Distribution
* Histogram + KDE visualization

### 4. Shape Metrics

* Skewness → detects asymmetry
* Kurtosis → detects extreme outliers

### 5. Standardization

* Z-score normalization

---

## 🔍 Pipeline Workflow

### Step 1: Data Loading

* Load dataset into Pandas DataFrame
* Basic inspection (`info`, `describe`)

---

### Step 2: Exploratory Data Analysis (EDA)

* Histogram + KDE plots
* Boxplots for outlier detection
* Statistical metrics:

  * Mean vs Median
  * Skewness
  * Kurtosis

---

### Step 3: Outlier Detection

Two approaches were compared:

#### Z-score Method

* Removes values beyond 3 standard deviations
* Assumes normal distribution

#### IQR Method

* Uses interquartile range
* More robust for skewed data

---

### Step 4: Handling Skewness

* Features with skewness > 1 were transformed
* Log transformation applied:

```
x → log(1 + x)
```

Result:

* Reduced skewness
* Improved symmetry

---

### Step 5: Feature Scaling

Standardization applied:

```
z = (x - mean) / std
```

Result:

* Mean ≈ 0
* Std ≈ 1
* Improved model stability

---

### Step 6: Model Training

Model used:

* Linear Regression

Evaluation:

* Train-test split
* R² score comparison

---

## 📈 Results

| Dataset Version      | Performance |
| -------------------- | ----------- |
| Raw Data             | Baseline    |
| Z-score Cleaned      | Improved    |
| IQR Cleaned          | More robust |
| Transformed + Scaled | Best        |

### Key Insight:

Proper preprocessing significantly improves model performance.

---

## 📊 Visualizations

The project includes:

* Distribution plots (before & after transformation)
* Boxplots (outlier detection)
* Correlation heatmap

---

## 🧪 Example Outputs

* Skewness reduction after log transform
* Outlier reduction using IQR
* Improved regression performance

---

## ⚙️ How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run main pipeline

```
python main.py
```

### 3. Run notebook (recommended)

```
jupyter notebook notebooks/analysis.ipynb
```

---

## 📦 Requirements

```
pandas
numpy
matplotlib
seaborn
scikit-learn
scipy
```

---

## 💡 Key Learnings

* Mean is sensitive to outliers → Median is more robust
* Skewed data can harm model performance
* Z-score works best for normal distributions
* IQR is better for real-world messy data
* Feature scaling is essential for many ML models

---

## 🔥 Future Improvements

* Add advanced models (Random Forest, XGBoost)
* Use automated pipelines (`sklearn.pipeline`)
* Add experiment tracking (MLflow)
* Deploy as an API (FastAPI)

---

## 🎯 Why This Project Matters

This project demonstrates:

* Strong understanding of **statistical foundations**
* Ability to **analyze real-world data**
* Knowledge of **ML preprocessing best practices**
* Practical implementation beyond tutorials

---

## 👨‍💻 Author

Abu Sayed

---

## ⭐ If you found this useful, consider giving it a star!
