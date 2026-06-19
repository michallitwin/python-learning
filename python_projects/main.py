from apscheduler.schedulers.blocking import BlockingScheduler
from api import OpenWeatherMap, NbpCurrency, CryptoAPI, Fear_Greed
from storage import TxtSaver, CsvSaver
from app import Daily_assistant

def run_daily_assistant():
    print("Cron Job: Running Daily Assistant.")
    
    weather_api = OpenWeatherMap("x")
    crypto_api = CryptoAPI("x")
    file_save = CsvSaver("notebook.csv")
    feargreed = Fear_Greed()
    currency_worker = NbpCurrency()
    assistant = Daily_assistant(weather_api, currency_worker, crypto_api, feargreed, file_save)

    #weather, currency, crypto, index
    assistant.start_aplication(category="crypto",crypto_name="Bitcoin")
    print("✅ Task executed successfully.")

scheduler = BlockingScheduler()

scheduler.add_job(run_daily_assistant, trigger='cron', minute='*/1')

print("Python Cron Scheduler started. [Press Ctrl+C to exit]")
run_daily_assistant()
scheduler.start()



