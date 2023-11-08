import datetime

import openweathermap
from config import settings


SPLIT_LINE = "-" * 40 + "\n"


def main():
    city = input("Введите город: ")
    print()

    current_city_weather = openweathermap.get_current_weather_by_city(
        api_key=settings.openweathermap_api_key,
        city=city
    )

    print("Город:", city)
    print("Время:", datetime.datetime.fromtimestamp(current_city_weather["timestamp"]))
    print("Погодные условия:", current_city_weather["description"])
    print("Видимость:", current_city_weather["visibility"], "метров")
    print("Скорость ветра:", current_city_weather["wind_speed"], "м/с")
    print("Температура:", current_city_weather["temperature"], "градусов")
    print("Минимальная температура:", current_city_weather["minimum_temperature"], "градусов")
    print("Максимальная температура", current_city_weather["maximum_temperature"], "градусов")
    print(SPLIT_LINE)

    forecast_city_weather = openweathermap.get_5day_forecast_weather_by_city(
        api_key=settings.openweathermap_api_key,
        city=city
    )

    for day_city_weather in forecast_city_weather:
        print("Время:", datetime.datetime.fromtimestamp(day_city_weather["timestamp"]))
        print("Погодные условия:", day_city_weather["description"])
        print("Видимость:", day_city_weather["visibility"], "метров")
        print("Скорость ветра:", day_city_weather["wind_speed"], "м/с")
        print("Температура:", day_city_weather["temperature"], "градусов")
        print("Минимальная температура:", day_city_weather["minimum_temperature"], "градусов")
        print("Максимальная температура", day_city_weather["maximum_temperature"], "градусов")
        print(SPLIT_LINE)


if __name__ == '__main__':
    main()
