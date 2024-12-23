# src/visualizations.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_age_sleep_quality(insights):
    """График зависимости качества сна от возраста"""
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Age', y='Sleep Quality', data=insights)
    plt.title('Age vs Sleep Quality')
    plt.xlabel('Age')
    plt.ylabel('Sleep Quality')
    plt.show()

def plot_activity_by_gender(insights):
    """График физической активности по полу"""
    plt.figure(figsize=(8, 6))
    insights.plot(kind='bar', stacked=True)
    plt.title('Physical Activity Level by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.show()

def plot_steps_by_sleep_disorders(insights):
    """График зависимости шагов от расстройств сна"""
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Sleep Disorders', y='Daily Steps', data=insights)
    plt.title('Daily Steps by Sleep Disorders')
    plt.xlabel('Sleep Disorders')
    plt.ylabel('Average Daily Steps')
    plt.show()

def plot_calories_by_medication(insights):
    """График сожженных калорий в зависимости от использования медикаментов"""
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Medication Usage', y='Calories Burned', data=insights)
    plt.title('Calories Burned by Medication Usage')
    plt.xlabel('Medication Usage')
    plt.ylabel('Average Calories Burned')
    plt.show()

def plot_sleep_quality_by_bedtime(insights):
    """График качества сна по времени отхода ко сну"""
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Bedtime', y='Sleep Quality', data=insights)
    plt.title('Sleep Quality by Bedtime')
    plt.xlabel('Bedtime')
    plt.ylabel('Sleep Quality')
    plt.show()
