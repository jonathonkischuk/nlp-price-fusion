import pandas as pd
from pathlib import Path


def merge_sentiment_price(ticker):
    price = pd.read_csv(f"data/prices/{ticker}.csv", parse_dates=["Date"])
    news = pd.read_csv(f"data/news/{ticker}_news.csv", parse_dates=["date"])

    sentiment_daily = news.groupby("date")["score"].mean().reset_index()
    sentiment_daily.columns = ["Date", "Sentiment"]

    price = price.merge(sentiment_daily, on="Date", how="left")
    price["Sentiment"].fillna(0, inplace=True)
    price["Target"] = price["Close"].shift(-1) > price["Close"]
    return price.dropna()
