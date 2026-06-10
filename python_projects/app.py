class Daily_assistant:
    def __init__(self, weather_provider, currency_provider, crypto_provider,saver):
        self.weather = weather_provider 
        self.currency = currency_provider
        self.crypto = crypto_provider
        self.saver = saver 


    def start_aplication(
            self,
            category:str,
            city:str = None, 
            currency_name:str = None, 
            crypto_name:str = None):
        
        if category == "weather":
            info = self.weather.get_weather(city)
            data = {city: info.temp}
        
        
        elif category == "currency":
            info = self.currency.get_currency(currency_name)
            data = {currency_name: info.curr}

        elif category == "crypto":
            info = self.crypto.get_crypto(crypto_name)
            data = {crypto_name: info.crypto }

        self.saver.save_data(data)
