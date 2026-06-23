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


class Fear_Greed_Data(BaseModel):
    value: int
    value_classification: str