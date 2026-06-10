from apscheduler.schedulers.blocking import BlockingScheduler
from api import OpenWeatherMap, NbpCurrency, CryptoAPI
from storage import TxtSaver, CsvSaver
from app import Daily_assistant

def run_daily_assistant():
    print("Cron Job: Running Daily Assistant.")
    
    api = OpenWeatherMap("x")
    api2 = CryptoAPI("x")
    file_save = TxtSaver("notebook.txt")
    currency_worker = NbpCurrency()
    assistant = Daily_assistant(api, currency_worker, api2, file_save)

    assistant.start_aplication(category="crypto", crypto_name="Bitcoin")
    print("✅ Task executed successfully.")

scheduler = BlockingScheduler()

scheduler.add_job(run_daily_assistant, trigger='cron', minute='*/1')

print("Python Cron Scheduler started. [Press Ctrl+C to exit]")
run_daily_assistant()
scheduler.start()