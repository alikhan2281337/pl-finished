import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Загрузка данных
data = pd.read_csv('processed_weather_data.csv')

# Создаём новую колонку с признаками — средней температурой
data['avg_temperature'] = (data['max_temperature'] + data['min_temperature']) / 2

# Целевая переменная — температура следующего дня
data['next_day_temperature'] = data['avg_temperature'].shift(-1)
data = data.dropna()  # Убираем строки с NaN

# Разделяем данные
X = data[['avg_temperature']]  # Признаки
y = data['next_day_temperature']  # Целевая переменная
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели
model = LinearRegression()
model.fit(X_train, y_train)

# Оценка модели
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")

# Сохранение модели
import joblib
joblib.dump(model, 'temperature_model.pkl')
print("Модель успешно обучена и сохранена!")
