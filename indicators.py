import ta

def add_moving_average(df):
    df["MA_20"] = df["Close"].rolling(20).mean()
    return df

def add_rsi(df):
    df["RSI"] = ta.momentum.RSIIndicator(df["Close"]).rsi()
    return df
