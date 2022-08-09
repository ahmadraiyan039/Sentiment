import tweepy
from textblob import TextBlob
from keys import user_access_token, user_access_secret, user_key, user_secret

auth = tweepy.OAuthHandler(user_key, user_secret)
auth.set_access_token(user_access_token, user_access_secret)

api = tweepy.API(auth)

lookUp = input("What tweet we looking for today?")
public_tweets = api.search_tweets(lookUp)
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)


