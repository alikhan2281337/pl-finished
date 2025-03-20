import pandas as pd

# Загружаем данные
df = pd.read_csv('weather_data.csv', delimiter=',')

# Убираем дублирующий столбец (если не нужен)
df = df.drop(columns=['date'])

# Проверяем результат
print("Исправленные данные:")
print(df.head())

# Сохраняем исправленный файл
df.to_csv('processed_weather_data.csv', index=False)
print("Файл сохранён как 'processed_weather_data.csv'")
