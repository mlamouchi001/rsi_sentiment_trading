RSI Sentiment Trading
Description
Ce projet combine l'analyse technique du RSI (Relative Strength Index) avec une analyse sentimentale avancée pour générer des signaux de trading sur la cryptomonnaie Bitcoin. Les données de sentiment proviennent de trois sources principales : Twitter, Reddit, et Discord, et sont analysées à l'aide du modèle BERT pour déterminer le sentiment global. Le projet intègre également des données de prix récupérées depuis Binance.

Composants principaux :
Analyse du RSI : Calcul du RSI à partir des données de prix historiques récupérées via Binance.
Analyse sentimentale avancée : Utilisation de BERT pour analyser les sentiments des messages sur Twitter, Reddit et Discord.
Décision de trading : Combinaison des résultats du RSI et du sentiment pour déterminer les signaux de trading (Acheter, Vendre, ou Ne rien faire).
Installation
Prérequis
Avant d'exécuter le projet, assurez-vous d'avoir :

Python 3.7 ou plus
Les clés API pour Twitter, Reddit, Discord, et Binance
Étapes d'installation
Cloner le dépôt :
bash
Copier le code
git clone https://github.com/yourusername/rsi_sentiment_trading.git
cd rsi_sentiment_trading
Créer et activer un environnement virtuel (optionnel mais recommandé) :
bash
Copier le code
python3 -m venv env
source env/bin/activate  # Sur Windows: env\Scripts\activate
Installer les dépendances :
Assurez-vous que toutes les dépendances nécessaires sont installées :

bash
Copier le code
pip install -r requirements.txt
Configurer les clés API :
Remplissez le fichier config.json avec vos propres clés API :

json
Copier le code
{
  "twitter": {
    "api_key": "YOUR_TWITTER_API_KEY",
    "api_secret": "YOUR_TWITTER_API_SECRET",
    "access_token": "YOUR_TWITTER_ACCESS_TOKEN",
    "access_secret": "YOUR_TWITTER_ACCESS_SECRET"
  },
  "reddit": {
    "client_id": "YOUR_REDDIT_CLIENT_ID",
    "client_secret": "YOUR_REDDIT_CLIENT_SECRET",
    "user_agent": "YOUR_REDDIT_USER_AGENT"
  },
  "discord": {
    "webhook_url": "YOUR_DISCORD_WEBHOOK_URL"
  },
  "binance": {
    "api_key": "YOUR_BINANCE_API_KEY",
    "api_secret": "YOUR_BINANCE_API_SECRET"
  }
}
Utilisation
Exécuter le script principal :
Une fois l'installation terminée et les configurations effectuées, vous pouvez exécuter le projet avec la commande suivante :

bash
Copier le code
python main.py
Processus global :
Le script va :
Récupérer les données de prix depuis Binance pour la paire BTC/USDT.
Calculer le RSI basé sur ces données.
Récupérer les tweets, posts Reddit, et messages Discord relatifs à Bitcoin.
Effectuer une analyse sentimentale sur ces messages en utilisant BERT.
Combiner les résultats du RSI et du sentiment pour générer une décision de trading :
Acheter : Lorsque le RSI est inférieur à 30 et que le sentiment global est positif.
Vendre : Lorsque le RSI dépasse 70 et que le sentiment est négatif.
Ne rien faire : Dans les autres cas.
Explication des fichiers
main.py : Le script principal qui orchestre le processus de collecte de données, d'analyse du RSI et des sentiments, et de prise de décision de trading.
scripts/collect_data.py : Récupère les données de Twitter, Reddit, et Discord ainsi que les prix depuis Binance.
models/sentiment_model.py : Utilise BERT pour analyser les sentiments des messages provenant de Twitter, Reddit, et Discord.
models/rsi_calculation.py : Calcule le RSI à partir des prix de clôture récupérés via Binance.
models/trading_decision.py : Génère une décision de trading en combinant les résultats du RSI et de l'analyse sentimentale.
config/config.json : Contient les clés API pour accéder à Twitter, Reddit, Discord et Binance.
requirements.txt : Liste des dépendances Python nécessaires pour exécuter le projet.
Fonctionnement
Stratégie de trading basée sur le RSI et le sentiment
RSI :

Si le RSI est inférieur à 30, cela peut indiquer une situation de survente (signal d'achat).
Si le RSI est supérieur à 70, cela peut indiquer une situation de surachat (signal de vente).
Sentiment :

Si le sentiment agrégé (moyenne des scores des tweets, posts Reddit, et messages Discord) est positif (> 0.5), cela renforce le signal d'achat.
Si le sentiment est négatif (< -0.5), cela renforce le signal de vente.
Combinaison RSI + Sentiment :

Si le RSI est bas (sous 30) et que le sentiment est positif, un signal d'achat est généré.
Si le RSI est haut (au-dessus de 70) et que le sentiment est négatif, un signal de vente est généré.
Dépendances
Les principales bibliothèques utilisées dans ce projet sont :

tweepy : Pour récupérer des tweets via l'API Twitter.
praw : Pour récupérer des posts Reddit.
requests : Pour accéder aux messages Discord via un webhook.
transformers : Pour l'analyse des sentiments avec BERT.
binance : Pour accéder aux données de prix via l'API Binance.
pandas : Pour manipuler et analyser les données.
Améliorations possibles
Modèle de prédiction des prix : Ajouter un modèle basé sur le Machine Learning ou le Deep Learning pour prédire les prix futurs.
Optimisation des seuils RSI : Tester et ajuster les seuils RSI pour correspondre aux conditions spécifiques du marché des cryptomonnaies.
Backtesting : Implémenter un backtesting complet sur plusieurs périodes et actifs pour valider la robustesse de la stratégie.
Ajout d'autres sources de données : Intégrer des sources de données supplémentaires comme les nouvelles économiques ou les discussions sur des forums spécialisés.
Auteurs
Votre Nom - Créateur du projet.
Licence
Ce projet est sous licence MIT. Vous pouvez librement l'utiliser, le modifier et le distribuer.

Remarques
Ce projet est fourni à titre expérimental et ne constitue en aucun cas un conseil financier. L'utilisateur est responsable de ses propres décisions de trading et des risques associés.

Ce fichier README.md vous fournira une documentation complète pour démarrer et exécuter votre projet. Assurez-vous de remplir le fichier config.json avec vos clés API avant de lancer le proje