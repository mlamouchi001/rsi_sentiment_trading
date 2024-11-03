import tweepy
import praw  # Pour Reddit
import requests  # Pour Discord
from binance.client import Client
import pandas as pd
import json

# Charger les clés API à partir de config.json
try:
    with open('config/config.json', 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    print("Le fichier config/config.json est introuvable.")
    exit(1)
except json.JSONDecodeError:
    print("Erreur de décodage JSON dans config/config.json.")
    exit(1)

# Récupération des données de Twitter
def fetch_tweets(query, count=100):
    try:
        auth = tweepy.OAuth1UserHandler(
            config['twitter']['api_key'],
            config['twitter']['api_secret'],
            config['twitter']['access_token'],
            config['twitter']['access_secret']
        )
        print("Authentification réussie.")
        api = tweepy.API(auth)
        print("Authentification réussie.22222222222222222")
        atwets = api.search_tweets(q=query, count=count , tweet_mode='extended')
        return [{"Text": tweet.full_text} for tweet in atwets]
    except tweepy.TwitterServerError as e:
        print(f"Erreur lors de la récupération des tweets: {e}")
        return []

# Récupération des données de Reddit
def fetch_reddit_posts(subreddit, limit=100):
    try:
        reddit = praw.Reddit(
            client_id=config['reddit']['client_id'],
            client_secret=config['reddit']['client_secret'],
            user_agent=config['reddit']['user_agent']
        )
        posts = reddit.subreddit(subreddit).new(limit=limit)
        return [{"Text": post.title + " " + post.selftext} for post in posts]
    except Exception as e:
        print(f"Erreur lors de la récupération des posts Reddit: {e}")
        return []

# Récupération des données de Discord via un webhook
def fetch_discord_messages(webhook_url):
    try:
        response = requests.get(webhook_url)
        response.raise_for_status()
        messages = response.json()
        return [{"Text": message['content']} for message in messages]
    except requests.RequestException as e:
        print(f"Erreur lors de la récupération des messages Discord: {e}")
        return []

# Sauvegarde des données récupérées dans un fichier CSV
def save_data(data, file_path):
    try:
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des données: {e}")

# Récupération des données de Binance
def get_binance_data(symbol, interval, start_date, end_date):
    try:
        client = Client(config['binance']['api_key'], config['binance']['api_secret'])
        klines = client.get_historical_klines(symbol, interval, start_date, end_date)
        df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume',
                                           'close_time', 'quote_asset_volume', 'number_of_trades',
                                           'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
        df['close'] = df['close'].astype(float)
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        return df[['close']]
    except Exception as e:
        print(f"Erreur lors de la récupération des données Binance: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    # Collecte des tweets
    tweets = fetch_tweets("Bitcoin", 100)
    save_data(tweets, "data/twitter_data.csv")

    # Collecte des posts Reddit
    reddit_posts = fetch_reddit_posts("cryptocurrency", 100)
    save_data(reddit_posts, "data/reddit_data.csv")

    # Collecte des messages Discord
    # discord_messages = fetch_discord_messages(config['discord']['webhook_url'])
    # save_data(discord_messages, "data/discord_data.csv")