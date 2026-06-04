import requests
from interfaces import WeatherProvider
from typing import Any
from pydantic import BaseModel, model_validator


class WeatherData(BaseModel):
    temp: float

    @model_validator(mode='before')
    @classmethod
    def weather_json(cls, data: dict):
        return {
            "temp": data["list"][0]["main"]["temp"]
        }

class NbpCurrencyData(BaseModel):
    curr: float 

    @model_validator(mode='before')
    @classmethod
    def curr_json(cls, data: dict):
        return {
            "curr": data["rates"][0]["mid"]
        }
        


class CryptoData(BaseModel):
    crypto: float

    @model_validator(mode='before')
    @classmethod
    def crypto_json(cls, data:dict):
        coin_id = list(data.keys())[0] 
    
        return {
        "crypto": data[coin_id]["pln"]
        }




class OpenWeatherMap(WeatherProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_weather(self, city: str) -> WeatherData:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.api_key}&units=metric"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        return WeatherData(**data)

class NbpCurrency:
    def get_currency(self, currency_name: str) -> NbpCurrencyData:
        url = f"https://api.nbp.pl/api/exchangerates/rates/a/{currency_name}/?format=json"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        return NbpCurrencyData(**data)
    

class CryptoAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key


    def get_crypto(self, crypto_name: str) -> CryptoData:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_name}&vs_currencies=pln&api_key={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        return CryptoData(**data)
    
