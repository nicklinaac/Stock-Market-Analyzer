import os
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator


def main():
    """Main function to fetch and analyze stock data."""
    csv_path = os.path.join("data", "symbols_valid_meta.csv")
    df = pd.read_csv(csv_path)
    input_ticker = input("Enter the ticker symbol (e.g., AAPL, NVDA, FB, etc.): ").strip().upper()
    input_timeline = input("Enter time period (e.g. 1mo, 6mo, 1y) or press ENTER for DEFAULT (3mo): ").strip()
    fetch_and_analyze(df,ticker_symbol=input_ticker, timeline=input_timeline)
    

def display_data(ticker_symbol, company_name,historical_data: pd.DataFrame) -> None:
    """Display the historical data in a readable format."""
    if historical_data.empty:
        print("No historical data available.")
    
    # Display a summary of the fetched data
    print(f"Summary of Historical Data for {ticker_symbol}:")
    print(historical_data[['Close', 'SMA20', 'SMA50', 'RSI', 'Signal']])

    # Plot closing price and moving averages
    plt.figure(figsize=(14, 8))
    plt.plot(historical_data.index, historical_data['Close'], label='Close Price', alpha=0.6)
    plt.plot(historical_data.index, historical_data['SMA20'], label='SMA20', linestyle='--')
    plt.plot(historical_data.index, historical_data['SMA50'], label='SMA50', linestyle='--')

    # Plot buy/sell signals
    buy_signals = historical_data[historical_data['Signal'] == 1]
    sell_signals = historical_data[historical_data['Signal'] == -1]
    plt.scatter(buy_signals.index, buy_signals['Close'], label='Buy Signal', marker='^', color='green')
    plt.scatter(sell_signals.index, sell_signals['Close'], label='Sell Signal', marker='v', color='red')

    plt.title(f"{company_name} ({ticker_symbol}) - SMA Crossover & RSI Strategy")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def fetch_and_analyze(df,ticker_symbol: str, timeline: str) -> None:
    try:
        if df.empty:
            raise ValueError("The metadata DataFrame is empty. Please check the CSV file.")
        if not ticker_symbol:
            raise ValueError("Ticker symbol cannot be empty.")
        if ticker_symbol not in df["Symbol"].values:
            raise ValueError(f"Ticker '{ticker_symbol}' not found in metadata.")
        if timeline == '':
            timeline = '3mo'  # Default to 3 months if no timeline is provided

        ticker = yf.Ticker(ticker_symbol)
        result = df[df["Symbol"] == ticker_symbol]
        company_name = result["Security Name"].values[0]

        print(f"\nFetching data for {ticker_symbol} - {company_name} ...")
        historical_data = ticker.history(period=timeline)

        if historical_data.empty:
            print("No data found.")
            raise ValueError("No historical data available for the specified ticker symbol and timeline.")

        # Calculate technical indicators
        # Calculate SMA (Simple Moving Average)
        historical_data['SMA20'] = None
        sma20 = SMAIndicator(close=historical_data['Close'], window=20)
        sma50 = SMAIndicator(close=historical_data['Close'], window=50)
        historical_data['SMA20'] = sma20.sma_indicator()
        historical_data['SMA50'] = sma50.sma_indicator()

        # Calculate RSI (Relative Strength Index) 
        rsi = RSIIndicator(close=historical_data['Close'])
        historical_data['RSI'] = rsi.rsi()

        # Signal logic
        historical_data['Signal'] = 0
        historical_data.loc[
            (historical_data['SMA20'] > historical_data['SMA50']) & (historical_data['RSI'] < 70), 'Signal'
        ] = 1  # Buy when SMA20 crosses above SMA50 and RSI is below 70
        historical_data.loc[
            (historical_data['SMA20'] < historical_data['SMA50']) | (historical_data['RSI'] > 70), 'Signal'
        ] = -1  # Sell when SMA20 crosses below SMA50 or RSI is above 70
        
        # Display the data
        display_data(ticker_symbol, company_name, historical_data)
        print("Data fetching complete.")
        

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
# Ensure the script runs only when executed directly