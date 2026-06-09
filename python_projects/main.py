from apscheduler.schedulers.blocking import BlockingScheduler
from api import OpenWeatherMap, NbpCurrency, CryptoAPI
from storage import FileSaver
from app import Daily_assistant

def run_daily_assistant():
    print("🤖 Cron Job: Running Daily Assistant...")
    
    # Initialize your classes (exactly like you did in main)
    api = OpenWeatherMap("x")
    api2 = CryptoAPI("CG-cpeRXg5Waey3tDosgtJvWFZJ")
    file_save = FileSaver("notebook.txt")
    currency_worker = NbpCurrency()
    assistant = Daily_assistant(api, currency_worker, api2, file_save)

    # Run the specific task
    assistant.start_aplication(category="crypto", crypto_name="Bitcoin")
    print("✅ Task executed successfully.")

# Initialize the scheduler
scheduler = BlockingScheduler()

# Cron Setup: e.g., minute='*/15' means it runs automatically every 15 minutes
scheduler.add_job(run_daily_assistant, trigger='cron', minute='*/1')

print("⏳ Python Cron Scheduler started... [Press Ctrl+C to exit]")
run_daily_assistant()
scheduler.start()