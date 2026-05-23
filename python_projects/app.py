class Daily_assistant:
    def __init__(self, weather_provider, currency_provider, saver):
        self.weather = weather_provider 
        self.currency = currency_provider
        self.saver = saver 


    def uruchom(self, category, target):
        if category == "weather":
            info = self.weather.get_weather(target)
            w = info["list"]
            text = f"Temperature in {target}: {w[0]['main']['temp']} °C"

        elif category == "currency":
            info = self.currency.get_currency(target)
            exchange = info["rates"][0]["mid"]
            text = f"Exchange: {target}: {exchange} PLN"
        

        self.saver.save_data(text)
