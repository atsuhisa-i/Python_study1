import schedule
import time
import scraping

schedule.every().day.at("00:16").do(scraping.job)

while True:
    schedule.run_pending()
    time.sleep(1)