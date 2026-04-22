from sklearn.linear_model import LinearRegression
import numpy as np

def predict_price(df):
    df = df.copy()

    # Create target column (next day's price)
    df["Target"] = df["Close"].shift(-1)

    # Remove empty rows
    df = df.dropna()

    X = np.array(df[["Close"]])
    y = np.array(df["Target"])

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Predict next value
    prediction = model.predict(X[-1].reshape(1, -1))

    return prediction[0]
