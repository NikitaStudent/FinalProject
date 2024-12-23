# src/data_cleaner.py
import pandas as pd

def clean_data(df):
    """Очищает данные"""
    # Преобразуем столбцы времени в datetime
    df['Bedtime'] = pd.to_datetime(df['Bedtime'], format='%H:%M', errors='coerce')
    df['Wake-up Time'] = pd.to_datetime(df['Wake-up Time'], format='%H:%M', errors='coerce')

    # Удалим строки с пропущенными значениями
    df = df.dropna()

    # Вернем очищенные данные
    return df
