from transformers import pipeline
import pandas as pd

# Initialisation du modèle BERT pour l'analyse des sentiments
sentiment_analyzer = pipeline('sentiment-analysis')

def analyze_sentiment(text):
    """
    Analyse du sentiment avec BERT.
    :param text: Texte à analyser
    :return: Score de sentiment (positif ou négatif)
    """
    result = sentiment_analyzer(text)[0]
    score = result['score'] if result['label'] == 'POSITIVE' else -result['score']
    return score

def analyze_file(input_file, output_file):
    """
    Analyse d'un fichier CSV pour détecter les sentiments et sauvegarde les résultats.
    :param input_file: Chemin du fichier d'entrée
    :param output_file: Chemin du fichier de sortie
    """
    df = pd.read_csv(input_file)
    df['Sentiment'] = df['Text'].apply(analyze_sentiment)
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    #analyze_file("data/twitter_data.csv", "data/processed_twitter_sentiment.csv")
    analyze_file("data/reddit_data.csv", "data/processed_reddit_sentiment.csv")
    ##analyze_file("data/discord_data.csv", "data/processed_discord_sentiment.csv")
