# Stock-Market-Analyzer
Personal Python project to analyze stock market trends

## 🧠 About

This project is designed to help me (and potentially others) understand stock market behavior by visualizing historical stock data for a given company. It fetches stock price data and outputs a graph showing price trends over time based on user input.

## 🚀 How to Use

1. Run the main script:
   ```bash
   python run_app.py
When prompted, enter:
A stock ticker symbol (e.g., AAPL for Apple, NVDA for Nvidia) **REQUIRED**
A time range (e.g., 1mo, 6mo, 1y) *optional*

If no input is provided, the default is 3 months.
The script will fetch the data and display a chart of the stock price over the specified timeframe.

📦 Requirements
Python 3.8+
Libraries:
pandas
matplotlib
yfinance

To install dependencies, run:
pip install -r requirements.txt

📁 Project Structure
project/
├── data/
│   └── symbols_valid_meta.csv
├── src/
│   └── fetch_and_analyze_data.py
├── run_app.py
├── requirements.txt
└── README.md

📝 Example Usage
$ python run_app.py
Enter the ticker symbol (e.g., AAPL, NVDA, FB, etc.): NVDA
Enter time period (e.g. 1mo, 6mo, 1y) or press ENTER for DEFAULT (3mo): 6mo
This will display a line graph of Nvidia’s stock over the past 6 months.

🔒 Disclaimer
This is a learning project and not intended as financial advice or for use in real-world trading.