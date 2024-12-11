# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 21:46:20 2024

@author: aoa
"""

import yfinance as yf
import streamlit as st

def get_stock_price(ticker):
    # Fetch live stock data
    stock = yf.Ticker(ticker)
    stock_info = stock.history(period="1d")
    if not stock_info.empty:
        return stock_info['Close'][-1]
    else:
        return None

def main():
    st.title("Live Stock Price Tracker")

    # Input for stock ticker symbol
    ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, MSFT):", "AAPL")

    if st.button("Get Stock Price"):
        try:
            price = get_stock_price(ticker)
            if price:
                st.success(f"The current price of {ticker} is ${price:.2f}")
            else:
                st.error("Unable to fetch stock data. Check the ticker symbol.")
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
