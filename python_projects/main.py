from api import OpenWeatherMap, NbpCurrency, CryptoAPI, Fear_Greed
from storage import TxtSaver, CsvSaver
from app import Daily_assistant

def run_daily_assistant():
    
    weather_api = OpenWeatherMap("x")
    crypto_api = CryptoAPI("x")
    file_save = CsvSaver("notebook.csv")
    feargreed = Fear_Greed()
    currency_worker = NbpCurrency()
    assistant = Daily_assistant(weather_api, currency_worker, crypto_api, feargreed, file_save)

    #weather, currency, crypto, index
    assistant.start_aplication(category="crypto",crypto_name="Bitcoin")



run_daily_assistant()




