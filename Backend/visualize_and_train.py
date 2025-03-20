import pandas as pd
import matplotlib.pyplot as plt

# Загружаем данные
df = pd.read_csv('processed_weather_data.csv')

# Проверяем данные
print(df.head())  # Выводим первые строки, чтобы убедиться, что всё в порядке

# Визуализация данных
plt.plot(df['time'], df['max_temperature'], label='Max Temperature', color='red')
plt.plot(df['time'], df['min_temperature'], label='Min Temperature', color='blue')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Trends')
plt.legend()
plt.xticks(rotation=45)  # Поворачиваем подписи по оси X для удобства чтения
plt.grid(True)  # Добавляем сетку
plt.tight_layout()  # Исправляем проблемы с разметкой
plt.show()
