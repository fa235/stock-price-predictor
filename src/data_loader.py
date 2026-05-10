import pandas as pd
import numpy as np

def load_stock_data(filepath):
    """load stock data from CSV file"""
    df = pd.read_csv(filepath)
    return df

def pre_process_data(filepath):
    """pre process data from CSV file"""
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.short_values('Date')
    return df

if __name__ == "__main__":
    print("Data loader module loaded successfully")