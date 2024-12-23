import sqlite3
import json
import pandas as pd
import numpy as np


def serialize_value(value):
    """
    Рекурсивное преобразование значений в JSON-сериализуемый формат.
    """
    if isinstance(value, pd.Series):
        return {k: serialize_value(v) for k, v in value.items()}
    elif isinstance(value, pd.DataFrame):
        return value.applymap(serialize_value).to_dict(orient='records')
    elif isinstance(value, pd.Timestamp):
        return value.isoformat()  # Преобразуем Timestamp в ISO строку
    elif isinstance(value, (np.int64, np.float64)):  # NumPy числа
        return value.item()
    elif isinstance(value, np.ndarray):
        return [serialize_value(v) for v in value]
    elif isinstance(value, dict):
        return {k: serialize_value(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [serialize_value(v) for v in value]
    else:
        # Для простых типов возвращаем значение напрямую
        return value


def save_insights_to_db(insights, db_name='health_and_sleep.db'):
    """
    Сохраняем инсайты в SQLite базу данных.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Создаем таблицу, если она не существует
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS insights (
        id INTEGER PRIMARY KEY,
        insight_name TEXT,
        value TEXT
    )
    ''')

    for insight_name, value in insights.items():
        try:
            # Преобразуем значение в JSON-совместимый формат
            serialized_value = json.dumps(serialize_value(value))

            # Вставляем данные
            cursor.execute('''
            INSERT INTO insights (insight_name, value)
            VALUES (?, ?)
            ''', (insight_name, serialized_value))
        except Exception as e:
            print(f"Ошибка при сериализации инсайта '{insight_name}': {e}")
            raise

    # Сохраняем изменения и закрываем соединение
    conn.commit()
    conn.close()
