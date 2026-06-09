from apscheduler.schedulers.blocking import BlockingScheduler

def fetch_market_data():
    print("Cron Job: Fetching latest market prices...")

scheduler = BlockingScheduler()

scheduler.add_job(fetch_market_data, trigger='cron', minute='*/1')

print("Python Cron Scheduler started... [Press Ctrl+C to exit]")
scheduler.start()