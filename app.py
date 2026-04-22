import streamlit as st

from data import get_stock_data
from indicators import add_moving_average, add_rsi
from visual import plot_stock
from model import predict_price

st.set_page_config(page_title="Stock Analyzer", layout="wide")

st.title("📊 Stock Market Analysis Tool")

# Inputs
ticker = st.text_input("Enter Stock Symbol", "AAPL")

period = st.selectbox(
    "Select Time Period",
    ["1mo", "3mo", "6mo", "1y", "5y"]
)

# Run analysis
if st.button("Analyze"):

    df = get_stock_data(ticker, period)

    df = add_moving_average(df)
    df = add_rsi(df)

    # Show data
    st.subheader("📄 Raw Data")
    st.dataframe(df.tail())

    # Chart
    st.subheader("📈 Price Chart")
    fig = plot_stock(df, ticker)
    st.plotly_chart(fig, use_container_width=True)

    # RSI
    st.subheader("📉 RSI Indicator")
    st.line_chart(df["RSI"])

    # 🔮 Prediction
    try:
        predicted_price = predict_price(df)
        st.subheader("🔮 Predicted Next Day Price")
        st.success(f"{predicted_price:.2f}")
    except:
        st.warning("Not enough data for prediction")
