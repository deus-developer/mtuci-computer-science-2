from typing import TypedDict, List

import requests

BASE_URL = 'https://api.openweathermap.org/'


class CityWeather(TypedDict):
    city: str
    timestamp: int
    description: str
    visibility: float
    temperature: float
    minimum_temperature: float
    maximum_temperature: float
    wind_speed: float


def get_current_weather_by_city(
    api_key: str,
    city: str
) -> CityWeather:
    response = requests.get(
        url=BASE_URL + 'data/2.5/weather',
        params={
            'q': city,
            'units': 'metric',
            'lang': 'ru',
            'appid': api_key
        }
    )
    response.raise_for_status()

    result = response.json()

    city_weather = CityWeather(
        city=city,
        timestamp=result['dt'],
        description=result['weather'][0]['description'],
        visibility=result['visibility'],
        temperature=result['main']['temp'],
        minimum_temperature=result['main']['temp_min'],
        maximum_temperature=result['main']['temp_max'],
        wind_speed=result['wind']['speed'],
    )
    return city_weather


def get_5day_forecast_weather_by_city(
    api_key: str,
    city: str
) -> List[CityWeather]:
    response = requests.get(
        url=BASE_URL + 'data/2.5/forecast',
        params={
            'q': city,
            'units': 'metric',
            'lang': 'ru',
            'appid': api_key
        }
    )
    response.raise_for_status()

    result = response.json()

    city_weather_forecast: List[CityWeather] = []

    for day_result in result['list']:
        city_weather = CityWeather(
            city=city,
            timestamp=day_result['dt'],
            description=day_result['weather'][0]['description'],
            visibility=day_result['visibility'],
            temperature=day_result['main']['temp'],
            minimum_temperature=day_result['main']['temp_min'],
            maximum_temperature=day_result['main']['temp_max'],
            wind_speed=day_result['wind']['speed'],
        )
        city_weather_forecast.append(city_weather)

    return city_weather_forecast
