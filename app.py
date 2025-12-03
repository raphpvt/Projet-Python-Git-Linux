import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Page configuration
st.set_page_config(page_title="Finance Dashboard", layout="wide")

st.title("Financial Dashboard - Project")
st.markdown("---")

# Sidebar for user inputs
st.sidebar.header("Settings")
# User inputs the asset symbol (default is Apple)
ticker = st.sidebar.text_input("Asset Symbol (e.g., AAPL, BTC-USD)", "AAPL")

# Manual refresh button
if st.sidebar.button("Refresh Data"):
    st.rerun()

# Data Retrieval (Real-time simulation)
# Retrieving 1 day of data with 5-minute intervals
data = yf.download(ticker, period="1d", interval="5m")

if not data.empty:
    # Get the latest closing price
    last_price = data['Close'].iloc[-1]
    
    # Display key metric
    st.metric(label=f"Current Price of {ticker}", value=f"{last_price:.2f} USD")
    
    # Interactive Plot using Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Price'))
    fig.update_layout(
        title=f"Intraday Evolution: {ticker}",
        xaxis_title="Time",
        yaxis_title="Price (USD)"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Display raw data in an expander
    with st.expander("View Raw Data"):
        st.dataframe(data)

else:
    # Error handling if the ticker is invalid
    st.error(f"Could not retrieve data for {ticker}. Please check the symbol.")
