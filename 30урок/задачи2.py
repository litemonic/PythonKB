import requests
from datetime import datetime

CITES = {
    "москва" : (55.7522, 37.6156),
    "екатеринбург": (56.8573, 60.6153),
    "санкт-петербург": (59.9386, 30.3141),
    "казань" : (55.7887, 49.1221),
    "киев" : (50.4547, 30.5238),
    "лондон" : (51.5085, -0.12574),
    "токио": (35.6895, 139.692)
}
url = "https://api.open-meteo.com/v1/forecast"

def GetForecast(cityName):
    cityKey = cityName.lower().strip()

    if cityKey not in CITES:
        print(f"Город {cityName} не найден в базе")
        print(f"Доступные города: {",".join(CITES.keys())}")
        return
    
    lat, lon = CITES[cityKey]

    params = {
        "latitude": lat,
        "longtitude" : lon,
        "current" : "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
        "timezone" : "auto",
        "wind_speed_unit": "ms",
        "temperature_unit": "celsius"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        current = data.get("current")

        if not current:
            print("нету данных о текущей погоде")
            return None
        
        temp = current.get("temperature_2m")
        humidity = current.get("relative_humidity_2m")
        wind = current.get("wind_speed_10m")
        weatherCode = current.get("weather_code")
        wearherD = decodeWeatherCode

        print("\n" + "=" * 40)
        print(f"погода: {cityName}")
        print(f"Время полученных данных: {datetime.now().strftime('%H:%M')}")
        print(f"Температура: {temp}")
        print(f"Влажность: {humidity}%")
        print(f"Состояние: {wind}")
        print(f"Ветер: {weatherCode}")
        print("\n" + "=" * 40)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        print("Проверьте интернет соеденение")

def decodeWeatherCode(code):
    code = {
        0 : "ясно",
        1 : "приемущественно ясно",
        2 : ""
    }
def main():
    print("Сервис погоды")
    print(f"Доступные города: {",".join(CITES.keys())}")

    while True:
        cityName = input("Введите название города (или exit): ")
        if cityName.lower() in ("exit", "quit", "выход", "0"):
            print("До свидания")
            break
        if not cityName:
            print("Введите название города!")
            continue
        GetForecast(cityName)
if __name__ == "__main__":
    main()