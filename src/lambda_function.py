import os
import random
import json
import tweepy
import datetime

# Build the tweet
def get_tweet():

    # Set the dates
    today = datetime.date.today()           # Today
    step1 = datetime.date(2021, 3, 29)      # Travel/5 friends
    step2 = datetime.date(2021, 5, 17)      # Groups up to 30
    step3 = datetime.date(2021, 6, 21)      # As many people as you like

    # Logic
    if today < step1:
        current = "In England we can ride locally, with 1 friend. "
        days = abs(step1 - today)
        if days.days == 1:
            future = "Tomorrow we will be able to travel within England and ride with 5 friends!"
        else:
            future = "In " + str(days.days) + " days we will be able to travel within England and ride with 5 friends!"
    elif today < step2:
        current = "In England we can travel within England and ride with 5 friends. "
        days = abs(step2 - today)
        if days.days == 1:
            future = "Tomorrow we will be able to ride in a group of up to 30 people, or travel abroad to ride."
        else:
            future = "In " + str(days.days) + " days we will be able to ride in a group of up to 30 people, or travel abroad to ride."
    elif today < step3:
        current = "In England we can travel within England and ride in a group of up to 30 people, or travel abroad to ride. "
        days = abs(step3 - today)
        if days.days == 1:
            future = "Tomorrow we will be able to ride with as many people as we want!"
        else:
            future = "In " + str(days.days) + " days we will be able to ride with as many people as we want!"
    else:
        current = "In England we can travel within England and ride with as many people as we want to. Or we can travel abroad to ride."
        future = ""
    
    tweet_text = current + future
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
