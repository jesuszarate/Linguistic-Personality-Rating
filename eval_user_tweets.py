# For tutorial go to https://www.youtube.com/watch?v=pUUxmvvl2FE

from __future__ import absolute_import, print_function
import sys
import urllib2

#tweepy
#from tweepy import Stream
#from tweepy import OAuthHandler
#from tweepy.streaming import StreamListener
import tweepy
from credentials import getConsumerKey
from credentials import getConsumerSecret
from credentials import getAccessToken
from credentials import getAccessSecret

consumer_key = getConsumerKey()
consumer_secret = getConsumerSecret()
access_token = getAccessToken()
access_secret = getAccessSecret()


'''
class listener(StreamListener):
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
'''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


stuff = api.user_timeline(screen_name = 'villordoos', count = 100, include_rts = True)

print(stuff)


