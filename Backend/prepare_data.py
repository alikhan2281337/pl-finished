import pandas as pd

# Указываем путь к вашему файлу
file_path = 'processed_weather_data.csv'

# Загрузка данных с указанием разделителя
data = pd.read_csv(file_path, sep=',')  # Измените `sep`, если разделитель другой
print("Изначальная структура данных:")
print(data.head())

# Переименовываем столбцы (если необходимо)
data.columns = ['time', 'max_temperature', 'min_temperature']  # Пример названий

# Добавляем среднюю температуру
data['avg_temperature'] = (data['max_temperature'] + data['min_temperature']) / 2

# Сохраняем преобразованный файл
data.to_csv('processed_weather_data.csv', index=False)
print("Данные успешно обработаны и сохранены в 'processed_weather_data.csv'")
