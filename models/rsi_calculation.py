import pandas as pd

def calculate_rsi(data, period=14):
    """
    Calcul du RSI à partir des prix de clôture.
    :param data: Série pandas avec les prix de clôture
    :param period: Période de calcul du RSI (par défaut 14)
    :return: Série pandas contenant le RSI
    """
    delta = data['close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

if __name__ == "__main__":
    df = pd.read_csv('data/historical_prices.csv')
    df['RSI'] = calculate_rsi(df)
    df.to_csv('data/historical_prices_with_rsi.csv', index=False)
