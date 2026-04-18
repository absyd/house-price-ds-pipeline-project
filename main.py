from sklearn.datasets import fetch_california_housing
import pandas as pd

from src.preprocessing import *
from src.modeling import train_model

# Load
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Process
df_clean = remove_outliers_iqr(df)
df_clean = fix_skewness(df_clean)

# Train
model, score = train_model(df_clean)

print("Final Score:", score)