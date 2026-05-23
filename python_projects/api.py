import requests
from interfaces import WeatherProvider

class OpenWeatherMap(WeatherProvider):
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, target):
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={target}&appid={self.api_key}&units=metric"

        response = requests.get(url)
        response.raise_for_status()

        return response.json()
    
class NbpCurrency:
    def get_currency(self, target):
        url = f"https://api.nbp.pl/api/exchangerates/rates/a/{target}/?format=json"

        response = requests.get(url)
        response.raise_for_status()

        return response.json()

