import time
import os
import sys
from apscheduler.schedulers.background import BackgroundScheduler
from loguru import logger

# Add parent paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def run_scraping_and_ingestion():
    logger.info("Starting scheduled scraping task...")
    try:
        from phase_1.scraper import scrape_mutual_funds
        scrape_mutual_funds()
        logger.info("Scraping completed successfully.")
        
        from phase_2.ingest import ingest_data
        ingest_data()
        logger.info("Data ingestion completed successfully.")
    except Exception as e:
        logger.error(f"Error in scheduled task: {str(e)}")

if __name__ == "__main__":
    logger.info("Initializing APScheduler...")
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_scraping_and_ingestion, 'interval', days=1)
    scheduler.start()
    logger.info("Scheduler started. Running first task immediately...")
    run_scraping_and_ingestion()
    
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        logger.info("Scheduler stopped.")
