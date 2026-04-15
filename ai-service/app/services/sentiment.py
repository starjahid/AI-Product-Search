from textblob import TextBlob

def sentiment_score(reviews):
    if not reviews:
        return 0.5

    total = 0

    for r in reviews:
        total += TextBlob(r).sentiment.polarity

    return (total / len(reviews) + 1) / 2