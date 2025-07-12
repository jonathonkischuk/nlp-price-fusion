from pipeline.scraper import scrape_all
from pipeline.sentiment import run_all_sentiments
from pipeline.feature_fusion import merge_sentiment_price
from pipeline.model import train_model
from plot import plot_sentiment_trend, plot_confusion_matrix
import yfinance as yf
import os
import pandas as pd


tickers = ["AMZN", "EPD", "ET", "GOOGL", "IBM", "META", "MSFT", "PG", "RGTI", "RITM", "TSM"]

os.makedirs("data/price", exist_ok=True)
for ticker in tickers:
    df = yf.download(ticker, start="2023-01-01")
    df.to_csv(f"data/prices/{ticker}.csv")


scrape_all(tickers)


run_all_sentiments()


for ticker in tickers:
    df = merge_sentiment_price(ticker)
    y_true, y_pred = train_model(df, ticker)

    plot_sentiment_trend(ticker)
    plot_confusion_matrix(y_true, y_pred, ticker)
    