import tweepy
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import pipeline
import time

# Configuration de l'API Twitter
API_KEY = '4QTjD4vJkAYoGmqNbfvucgdrp'
API_SECRET_KEY = 'nU7VD7AZVSaeZ2EQw3GfYzaMYm9uvAxOg9LEqoEHAiUgZY2zYw'
ACCESS_TOKEN = '792057852336668672-eGs0PzExih0ZbK5N8DVwx9SCEoY5dfc'
ACCESS_TOKEN_SECRET = 'atQObaqtTmDx86Z9Qu4h4WVU1kmc1fOXiC7hWlf11qI82'

# Authentification à l'API Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Charger le modèle BERT pré-entraîné
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"  # Modèle pré-entraîné pour l'analyse de sentiment
sentiment_pipeline = pipeline("sentiment-analysis", model=model_name)

# Fonction pour obtenir les tweets sur une crypto-monnaie
def get_tweets(crypto_symbol, count=100):
    tweets = api.search_tweets(q=crypto_symbol, count=count, lang='en', tweet_mode='extended')
    return tweets

# Fonction pour analyser le sentiment des tweets
def analyze_sentiment(tweets):
    positive_count = 0
    negative_count = 0
    neutral_count = 0

    for tweet in tweets:
        result = sentiment_pipeline(tweet.full_text)
        sentiment = result[0]

        # Classifier le sentiment
        if sentiment['label'] == 'POSITIVE':
            positive_count += 1
        elif sentiment['label'] == 'NEGATIVE':
            negative_count += 1
        else:
            neutral_count += 1

    return positive_count, negative_count, neutral_count

# Fonction principale
def main():
    crypto_symbol = 'Bitcoin'  # Remplacez par la crypto que vous souhaitez suivre
    while True:
        tweets = get_tweets(crypto_symbol)
        positive, negative, neutral = analyze_sentiment(tweets)

        print(f"Sentiment sur {crypto_symbol}:")
        print(f"Positifs: {positive}, Négatifs: {negative}, Neutres: {neutral}")

        # Logique de trading simple
        if positive > negative:
            print("Sentiment positif détecté, considérer d'acheter.")
        elif negative > positive:
            print("Sentiment négatif détecté, considérer de vendre.")
        else:
            print("Sentiment neutre, aucune action recommandée.")

        # Attendre avant de vérifier à nouveau
        time.sleep(600)  # Vérifier toutes les 10 minutes

if __name__ == "__main__":
    main()