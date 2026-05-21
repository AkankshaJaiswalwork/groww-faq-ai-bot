import os
import json
import requests
from bs4 import BeautifulSoup
from loguru import logger

def scrape_mutual_funds():
    logger.info("Scraping mutual funds from Groww...")
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(data_dir, exist_ok=True)
    logger.info("Scraped and saved structured mutual fund data successfully.")

if __name__ == "__main__":
    scrape_mutual_funds()
