# For tutorial go to https://www.youtube.com/watch?v=pUUxmvvl2FE

from __future__ import absolute_import, print_function
import sys

#tweepy
import tweepy
import json
from credentials import getConsumerKey
from credentials import getConsumerSecret
from credentials import getAccessToken
from credentials import getAccessSecret

consumer_key = getConsumerKey()
consumer_secret = getConsumerSecret()
access_token = getAccessToken()
access_secret = getAccessSecret()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def getTweets(user_handler):
    stuff = api.user_timeline(screen_name = user_handler, count = 100, include_rts = True)

    tweets = ''
    for s in stuff:
        status = s
        
        jsonStr = json.dumps(status._json)
        j = json.loads(jsonStr)

        t = j['text']
        print (t)
        tweets += t + '\n'


    print (tweets)

    clean_tweets = tweets.encode('ascii', 'ignore').decode('ascii')
    with open('output.txt', 'w') as f:
        f.write(clean_tweets)


getTweets('villordoos')
