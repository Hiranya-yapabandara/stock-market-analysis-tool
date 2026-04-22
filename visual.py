import plotly.graph_objects as go

def plot_stock(df, ticker):
    fig = go.Figure()

    # Price line
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df["Close"],
        name="Close Price"
    ))

    # Moving Average
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df["MA_20"],
        name="MA 20"
    ))

    # 🔥 Improved UI
    fig.update_layout(
        template="plotly_dark",
        title=f"{ticker} Stock Price",
        xaxis_title="Date",
        yaxis_title="Price",
        legend_title="Indicators"
    )

    return fig
