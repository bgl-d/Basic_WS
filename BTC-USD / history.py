import yfinance as yf
import matplotlib.pyplot as plt

ticker_symbol = "BTC-USD"
BTC = yf.Ticker(ticker_symbol)
BTC_price_data = BTC.history(period="1y")  # Fetch data for the last year

if BTC_price_data.empty:
    print(f"Error: Unable to retrieve data for {ticker_symbol} ticker.")
else:
    BTC_price_data.reset_index(inplace=True)  # Reset index to use "Date" as a column
    BTC_price_data.plot(x="Date", y="Open")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.title(f"{ticker_symbol} Opening Price")
    plt.show()