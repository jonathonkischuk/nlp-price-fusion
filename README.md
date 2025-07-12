# 💬 NLP Price Fusion Model

This project fuses **real-time financial news sentiment** with **stock price data** using a transformer-based NLP model to generate enhanced trading signals for event-driven strategies. It combines **web scraping**, **sentiment analysis (Hugging Face)**, **tabular price features**, and a **machine learning classifier** to create predictive insights.

---

## 🔧 Features

- ✅ Real-time web scraping of financial headlines (Yahoo Finance)
- ✅ Sentiment scoring using Hugging Face transformers (`distilbert-base-uncased-finetuned-sst-2-english`)
- ✅ Fusion of price action with sentiment data for modeling
- ✅ Target labeling using next-day price movement
- ✅ RandomForest classifier for up/down direction prediction
- ✅ Visualizations:
  - Daily sentiment trends
  - Confusion matrix for prediction diagnostics
- ✅ Dockerized and automated via `main.py`

---

## 📈 Assets Covered

**Stock Tickers Tracked:**

AMZN, EPD, ET, GOOGL, IBM, META, MSFT, PG, RGTI, RITM, TSM


These tickers are used for both historical price collection and real-time news scraping over the past ~6 months.

---

## ▶️ Usage

### ✅ Run Locally

```bash
# Clone repo and enter directory
git clone https://github.com/your-username/nlp-price-fusion.git
cd nlp-price-fusion

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the complete pipeline
python main.py

```

### ✅ Run with Docker

```bash
# Build & Run Container
docker build -t nlp-price-fusion .
docker run --rm nlp-price-fusion

```
