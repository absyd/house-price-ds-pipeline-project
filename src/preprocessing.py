import numpy as np
import pandas as pd
from scipy.stats import skew, zscore

def remove_outliers_z(df):
    z = np.abs(zscore(df))
    return df[(z < 3).all(axis=1)]

def remove_outliers_iqr(df):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    
    return df[~((df < (Q1 - 1.5 * IQR)) | 
                (df > (Q3 + 1.5 * IQR))).any(axis=1)]

def fix_skewness(df):
    df = df.copy()
    
    for col in df.columns:
        if abs(skew(df[col])) > 1:
            df[col] = np.log1p(df[col])
    
    return df