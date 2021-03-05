import os
import random
import json
import tweepy

def get_tweet():
    """Get tweet to post from CSV file"""

    tweet_text = "In England we can ride locally, with 1 friend. "

    return tweet_text


def lambda_handler(event, context):
    print("Get credentials")
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    print("Authenticate")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    print("Get tweet")
    tweet = get_tweet()

    print(f"Post tweet: {tweet}")
    # api.update_status(tweet)

    return {"statusCode": 200, "tweet": tweet}
