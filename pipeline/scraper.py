import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path
import time


def scrape_yahoo_finance(ticker, days=180):
    url = f"https://finance.yahoo.com/quote/{ticker}/news?p={ticker}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    all_news = []

    for page in range(1, 5):
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "lxml")
        articles = soup.select("li.js-stream-content")

        for article in articles:
            headline = article.find("h3")
            timestamp = article.find("time")
            if headline and timestamp:
                text = headline.text.strip()
                date = timestamp['datetime'].split("T")[0]
                all_news.append((date, text))

        time.sleep(1)

    df = pd.DataFrame(all_news, columns=['date', 'headline'])
    df['ticker'] = ticker
    return df


def scrape_all(tickers):
    news_path = Path("data/news")
    news_path.mkdir(parents=True, exist_ok=True)

    for ticker in tickers:
        print(f"Scraping {ticker}...")
        df = scrape_yahoo_finance(ticker)
        df.to_csv(news_path / f"{ticker}_news.csv", index=False)

        