from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import pandas as pd


def train_model(df, ticker):
    features = ["Open", "High", "Low", "Close", "Volume", "Sentiment"]
    X = df[features]
    y = df["Target"].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f"\n[{ticker}] Results:\n")
    print(classification_report(y_test, y_pred))

    return y_test, y_pred

