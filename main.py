from scripts.collect_data import get_binance_data, fetch_tweets, fetch_reddit_posts, fetch_discord_messages, save_data
from models.sentiment_model import analyze_file
from models.rsi_calculation import calculate_rsi
from models.trading_decision import trading_decision
import pandas as pd

# 1. Récupérer les données de Binance
symbol = 'BTCUSDT'
interval = '1h'
start_date = "1 Jan 2023"
end_date = "1 Oct 2023"
df = get_binance_data(symbol, interval, start_date, end_date)

# 2. Calculer le RSI
df['RSI'] = calculate_rsi(df)

# 3. Collecter des tweets, posts Reddit et messages Discord
#tweets = fetch_tweets("Bitcoin", 100)
#save_data(tweets, "data/twitter_data.csv")

reddit_posts = fetch_reddit_posts("cryptocurrency", 100)
save_data(reddit_posts, "data/reddit_data.csv")

#discord_messages = fetch_discord_messages("YOUR_DISCORD_WEBHOOK_URL")
#save_data(discord_messages, "data/discord_data.csv")

# 4. Analyser les sentiments
#analyze_file("data/twitter_data.csv", "data/processed_twitter_sentiment.csv")
analyze_file("data/reddit_data.csv", "data/processed_reddit_sentiment.csv")
#analyze_file("data/discord_data.csv", "data/processed_discord_sentiment.csv")

# 5. Calculer le score moyen de sentiment
twitter_sentiment = pd.read_csv("data/processed_twitter_sentiment.csv")['Sentiment'].mean()
reddit_sentiment = pd.read_csv("data/processed_reddit_sentiment.csv")['Sentiment'].mean()
discord_sentiment = pd.read_csv("data/processed_discord_sentiment.csv")['Sentiment'].mean()
sentiment_score = (twitter_sentiment + reddit_sentiment + discord_sentiment) / 3

# 6. Prendre des décisions de trading
latest_rsi = df['RSI'].iloc[-1]  # Dernier RSI
decision = trading_decision(0, sentiment_score, latest_rsi)
print(f"RSI actuel : {latest_rsi:.2f}, Sentiment moyen : {sentiment_score:.2f}, Décision de trading : {decision}")
