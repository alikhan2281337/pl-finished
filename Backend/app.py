from flask import Flask, request, jsonify
import requests
import joblib  # Для загрузки модели

app = Flask(__name__)

API_KEY = "43f676203e7fd5d60bf557d60902a3e4"  # Твой ключ от OpenWeatherMap

# Загрузка ML модели
model = joblib.load('temperature_model.pkl')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')  # Считываем параметр "city"
    if not city:
        return jsonify({'error': 'Город не указан'}), 400

    # Запрос на OpenWeatherMap
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(api_url, params=params)

    if response.status_code != 200:
        return jsonify({'error': 'Не удалось найти данные по городу'}), response.status_code

    data = response.json()

    # Формируем ответ
    result = {
        "city": data["name"],
        "temperature": round(data["main"]["temp"]),
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "icon": data["weather"][0]["icon"]
    }

    return jsonify(result)

@app.route('/predict_temperature', methods=['POST'])
def predict_temperature():
    # Получаем данные от клиента
    data = request.get_json()
    if not all(key in data for key in ['humidity', 'pressure', 'wind_speed']):
        return jsonify({'error': 'Необходимо указать влажность, давление и скорость ветра'}), 400

    features = [[data['humidity'], data['pressure'], data['wind_speed']]]
    prediction = model.predict(features)

    return jsonify({'predicted_temperature': prediction[0]})

# Новый маршрут для предсказания на основе среднего значения температуры
@app.route('/predict_avg_temperature', methods=['POST'])
def predict_avg_temperature():
    # Получаем данные от клиента
    data = request.get_json()
    if 'avg_temperature' not in data:
        return jsonify({'error': 'Необходимо указать avg_temperature'}), 400

    # Предсказание
    features = [[data['avg_temperature']]]
    prediction = model.predict(features)

    return jsonify({'predicted_temperature': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
