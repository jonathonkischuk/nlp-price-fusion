from transformers import pipeline
import pandas as pd
from pathlib import Path


def score_sentiment(file):
    df = pd.read_csv(file)
    nlp = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    df["sentiment"] = df["headline"].apply(lambda x: nlp(x[:512])[0]["label"])
    df["score"] = df["headline"].apply(lambda x: nlp(x[:512])[0]["score"])
    df["score"] = df.apply(lambda row: row["score"] if row["sentiment"] == "POSITIVE" else -row["score"], axis=1)
    return df


def run_all_sentiments():
    path = Path("data/news")
    for file in path.glob("*.csv"):
        df = score_sentiment(file)
        df.to_csv(file, index=False)
        