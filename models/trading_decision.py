def trading_decision(price_prediction, sentiment_score, rsi, rsi_buy_threshold=30, rsi_sell_threshold=70):
    """
    Prendre une décision de trading en fonction du RSI et du sentiment.
    :param price_prediction: Prédiction du prix
    :param sentiment_score: Score de sentiment agrégé
    :param rsi: Valeur actuelle du RSI
    :param rsi_buy_threshold: Seuil RSI pour acheter (par défaut 30)
    :param rsi_sell_threshold: Seuil RSI pour vendre (par défaut 70)
    :return: 'Acheter', 'Vendre' ou 'Ne rien faire'
    """
    if rsi < rsi_buy_threshold and sentiment_score > 0.5:
        return "Acheter"
    elif rsi > rsi_sell_threshold and sentiment_score < -0.5:
        return "Vendre"
    else:
        return "Ne rien faire"
