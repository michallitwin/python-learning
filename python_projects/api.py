import requests


class OpenWeatherMap(WeatherProvider):
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, location):
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={self.api_key}&units=metric"

        response = requests.get(url)
        response.raise_for_status()

        return response.json()