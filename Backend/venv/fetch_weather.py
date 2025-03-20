import requests
import pandas as pd

# Параметры запроса
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 42.87,  # Координаты Бишкека
    "longitude": 74.59,
    "start_date": "2024-01-01",  # Дата начала
    "end_date": "2024-01-10",    # Дата конца
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "auto"
}

# Отправка запроса
response = requests.get(url, params=params)

# Проверка ответа
if response.status_code == 200:
    data = response.json()
    print("Данные успешно получены.")

    # Преобразуем данные в DataFrame
    df = pd.DataFrame(data['daily'])
    df['date'] = data['daily']['time']  # Добавляем дату
    df = df.rename(columns={
        'temperature_2m_max': 'max_temperature',
        'temperature_2m_min': 'min_temperature'
    })

    # Сохраняем данные в CSV
    df.to_csv('weather_data.csv', index=False)
    print("Данные сохранены в файл weather_data.csv")
else:
    print(f"Ошибка: {response.status_code}")
