# FinalProject.py

import os
from src.data_loader import load_data
from src.data_cleaner import clean_data
from src.insights_generator import generate_insights
from src.visualizations import (
    plot_age_sleep_quality, plot_activity_by_gender,
    plot_steps_by_sleep_disorders, plot_calories_by_medication,
    plot_sleep_quality_by_bedtime
)
from src.sqlite_db import save_insights_to_db

# Указываем путь к файлу с данными
file_path = os.path.join('data', 'Health_Sleep_Statistics.csv')

# Загружаем и очищаем данные
df = load_data(file_path)
df = clean_data(df)

# Генерируем инсайты
insights = generate_insights(df)

# Визуализируем инсайты
plot_age_sleep_quality(insights['age_sleep_quality'])
plot_activity_by_gender(insights['activity_by_gender'])
plot_steps_by_sleep_disorders(insights['steps_by_sleep_disorders'])
plot_calories_by_medication(insights['calories_by_medication'])
plot_sleep_quality_by_bedtime(insights['sleep_quality_by_bedtime'])

# Сохраняем инсайты в базу данных
save_insights_to_db(insights)
