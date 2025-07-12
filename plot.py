import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def plot_sentiment_trend(ticker):
    df = pd.read_csv(f"data/news/{ticker}_news.csv", parse_dates=["date"])
    sentiment_daily = df.groupby("date")["score"].mean()

    plt.figure(figsize=(12, 6))
    plt.plot(sentiment_daily.index, sentiment_daily.values, label="Avg Daily Sentiment")
    plt.title(f"Daily Sentiment Trend - {ticker}")
    plt.xlabel("Date")
    plt.ylabel("Sentiment Score")
    plt.axhline(0, color='gray', linestyle='--')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"reports/{ticker}_sentiment_trend.png")
    plt.show()


def plot_confusion_matrix(y_true, y_pred, ticker):
    cm = confusion_matrix(y_true, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Down", "Up"])
    disp.plot(cmap="Blues", values_format="d")
    plt.title(f"Prediction Confusion Matrix - {ticker}")
    plt.savefig(f"reports/{ticker}_confusion_matrix.png")
    plt.show()
    plt.close()