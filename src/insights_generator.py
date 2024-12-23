# src/insights_generator.py

def generate_insights(df):
    """Генерирует инсайты из данных"""

    insights = {}

    # Пример инсайта: среднее качество сна по возрасту
    age_sleep_quality = df.groupby('Age')['Sleep Quality'].mean().reset_index()
    insights['age_sleep_quality'] = age_sleep_quality

    # Пример инсайта: средний уровень физической активности по полу
    activity_by_gender = df.groupby('Gender')['Physical Activity Level'].value_counts().unstack().fillna(0)
    insights['activity_by_gender'] = activity_by_gender

    # Пример инсайта: зависимость шагов от расстройств сна
    steps_by_sleep_disorders = df.groupby('Sleep Disorders')['Daily Steps'].mean().reset_index()
    insights['steps_by_sleep_disorders'] = steps_by_sleep_disorders

    # Пример инсайта: зависимость сожженных калорий от использования медикаментов
    calories_by_medication = df.groupby('Medication Usage')['Calories Burned'].mean().reset_index()
    insights['calories_by_medication'] = calories_by_medication

    # Пример инсайта: качество сна по времени отхода ко сну
    sleep_quality_by_bedtime = df.groupby('Bedtime')['Sleep Quality'].mean().reset_index()
    insights['sleep_quality_by_bedtime'] = sleep_quality_by_bedtime

    return insights
