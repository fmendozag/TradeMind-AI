# services/data_collector.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("API_URL")

def get_market_data(symbol="EURUSD", timeframe="1m"):
    url = f"{BASE_URL}/marketdata?symbol={symbol}&timeframe={timeframe}&apikey={API_KEY}"
    response = requests.get(url)
    return response.json()
