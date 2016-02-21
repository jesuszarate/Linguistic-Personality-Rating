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
from xml_parser import get_categories
from personality_calc import rate_tweet
from trait_definitions import getDefinitions

consumer_key = getConsumerKey()
consumer_secret = getConsumerSecret()
access_token = getAccessToken()
access_secret = getAccessSecret()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


# Get the location and map it to the word count of the tweet                                                                                                  
def map_to_count(s):
        word_list = s.split(' ')
        result_d = dict([])
        for word in word_list:
                word = word.lower()
                if(word in result_d):
                        result_d[word] += 1
                else:
                        result_d[word] = 1
        return (result_d)


def getTweets(user_handler):
    stuff = api.user_timeline(screen_name = user_handler, count = 2000, include_rts = True)

    tweets = ''
    for s in stuff:
        status = s
        
        jsonStr = json.dumps(status._json)
        j = json.loads(jsonStr)
        t = j['text']
        #print (t)
        tweets += t


    #print (tweets)

    clean_tweets = tweets.encode('ascii', 'ignore').decode('ascii')
    with open('output.txt', 'w') as f:
        f.write(clean_tweets)

    return clean_tweets


def findMax(rating):
    max = ('ps', rating['ps'])
    #import pdb; pdb.set_trace()
    #for r in rating:
    for key, value in rating.items():
        if max[1] < value:
            max = (key, value)      
    return max[0]


def rateTweets(user_handler):
    cats = get_categories()
    #tweets = getTweets('villordoos')
    tweets = getTweets(user_handler)

    map_tweets = map_to_count(tweets)
    print ("\n\n\t")
    #print (getDefinitions())

    rating = rate_tweet(map_tweets, cats)
    
    print ('\n\n')
    #print (findMax(rating))
    max_rtng = findMax(rating)
    definition = getDefinitions()[max_rtng]
    print (definition)
    print ('\n\n')

    print (rating)
    print ("\n\n")

if len(sys.argv) > 1:
    rateTweets(sys.argv[1])
else:
    print ('\n\n\tMust provide a user hanlder as a parameter to rate\n\n')
