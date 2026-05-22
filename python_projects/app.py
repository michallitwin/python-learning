class WeatherApp:
    def __init__(self, provider, saver):
        self.provider = provider # Twój pracownik od internetu
        self.saver = saver # Twój pracownik od zapisu na dysk


    def uruchom(self, location):
        info = self.provider.get_weather(location)

        w = info["list"]
        print(f"Temperature: {w[0]['main']['temp']} °C")


        self.saver.save_data(info)
