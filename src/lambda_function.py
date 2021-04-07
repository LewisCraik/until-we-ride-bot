import os
import random
import json
import tweepy
import datetime

# Build the tweet
def get_tweet():

    # Set the dates
    today = datetime.date.today()           # Today
    dTravel = datetime.date(2021, 3, 29)    # Travel/5 friends
    dWales = datetime.date(2021, 4, 12)     # Travel to Wales
    dGroup = datetime.date(2021, 5, 17)     # Groups up to 30
    dFreedom = datetime.date(2021, 6, 21)   # As many people as you like

    # Logic
    if today < dTravel:
        current = "In England we can ride locally, with 1 friend. "
        days = abs(dTravel - today)
        if days.days == 1:
            future = "Tomorrow we will be able to travel within England and ride with 5 friends!"
        else:
            future = "In " + str(days.days) + " days we will be able to travel within England and ride with 5 friends!"
    elif today < dWales:
        current = "In England we can travel within England and ride with 5 friends. "
        days = abs(dWales - today)
        if days.days == 1:
            future = "Tomorrow we will also be able to travel to Wales."
        else:
            future = "In " + str(days.days) + " days we will also be able to travel to Wales."
    elif today < dGroup:
        current = "In England we can travel within England and Wales to ride with 5 friends. "
        days = abs(dGroup - today)
        if days.days == 1:
            future = "Tomorrow we will be able to ride in a group of up to 30 people, or travel abroad to ride."
        else:
            future = "In " + str(days.days) + " days we will be able to ride in a group of up to 30 people, or travel abroad to ride."
    elif today < dFreedom:
        current = "In England we can travel within England and Wales, and ride in a group of up to 30 people, or travel abroad to ride. "
        days = abs(dFreedom - today)
        if days.days == 1:
            future = "Tomorrow we will be able to ride with as many people as we like!"
        else:
            future = "In " + str(days.days) + " days we will be able to ride with as many people as we like!"
    else:
        current = "In England we can travel within England and Wales to ride with as many people as we want to. Or we can travel abroad to ride."
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
    print(f"Tweet length: {len(tweet)}")
    api.update_status(tweet)
    
    return {"statusCode": 200, "tweet": tweet}
