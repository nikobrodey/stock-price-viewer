import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

def main():
    st.title("Stock Price Viewer")

    # User inputs
    ticker = st.text_input("Enter stock ticker (e.g., AAPL, GOOGL):", "AAPL")
    duration = st.selectbox("Select time duration:", ["1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"])

    if st.button("Show Chart"):
        # Fetch stock data
        stock_data = yf.Ticker(ticker).history(period=duration)

        # Create interactive chart
        fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                             open=stock_data['Open'],
                                             high=stock_data['High'],
                                             low=stock_data['Low'],
                                             close=stock_data['Close'])])
        fig.update_layout(title=f"{ticker} Stock Price", xaxis_title="Date", yaxis_title="Price")

        # Display chart
        st.plotly_chart(fig)

        # Display recent performance
        st.subheader("Recent Performance")
        st.dataframe(stock_data.tail())

if __name__ == "__main__":
    main()