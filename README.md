# Stock-Market-Analyzer

Personal Python project to analyze stock market trends


## 🧠 About

This project is designed to help me (and potentially others) understand stock market behavior by visualizing historical stock data for a given company. It fetches stock price data and outputs a graph showing price trends over time based on user input.


## 🚀 How to Use

To deploy this project, run the main script:

```bash
  python run_app.py
```

## 📦 Requirements

**Python 3.8+** 

**Libraries:**
- yfinance
- pandas
- numpy
- matplotlib
- plotly
- seaborn
- ta


To install dependencies, run:

```bash
  pip install -r requirements.txt

```
## 📝 Example Usage

```bash
Enter the ticker symbol (e.g., AAPL, NVDA, FB, etc.): AAPL
Enter time period (e.g. 1mo, 6mo, 1y) or press ENTER for DEFAULT (3mo): 1y

Fetching data for AAPL - Apple Inc. - Common Stock ...
Summary of Historical Data for AAPL:
                                Close       SMA20       SMA50        RSI  Signal
Date
2024-06-06 00:00:00-04:00  193.574692         NaN         NaN        NaN       0
2024-06-07 00:00:00-04:00  195.973495         NaN         NaN        NaN       0
2024-06-10 00:00:00-04:00  192.221024         NaN         NaN        NaN       0
2024-06-11 00:00:00-04:00  206.185715         NaN         NaN        NaN       0
2024-06-12 00:00:00-04:00  212.078201         NaN         NaN        NaN       0
...                               ...         ...         ...        ...     ...
2025-05-30 00:00:00-04:00  200.850006  203.400248  205.206494  45.832349      -1
2025-06-02 00:00:00-04:00  201.699997  203.231194  204.964102  46.999536      -1
2025-06-03 00:00:00-04:00  203.270004  203.463218  204.669819  49.177875      -1
2025-06-04 00:00:00-04:00  202.820007  203.691718  204.317401  48.561801      -1
2025-06-05 00:00:00-04:00  200.630005  203.923569  203.860862  45.569809       1

[250 rows x 5 columns]
Data fetching complete.
```
    
## 🔒 Disclaimer

This is a learning project and not intended as financial advice or for use in real-world trading.