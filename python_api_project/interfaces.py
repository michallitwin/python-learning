from abc import ABC, abstractmethod


class WeatherProvider(ABC):
    
    @abstractmethod  
    def get_weather(self, location):
        pass


class DataSaver(ABC):

    @abstractmethod
    def save_data(self, data):
        pass