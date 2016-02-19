# For tutorial go to https://www.youtube.com/watch?v=pUUxmvvl2FE

import sys
import urllib2

#tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from credentials import getConsumerKey
from credentials import getConsumerSecret
from credentials import getAccessToken
from credentials import getAccessSecret


consumerKey = getConsumerKey()
consumerSecret = getConsumerSecret()
accessToken = getAccessToken()
accessSecret = getAccessSecret()


class listener(StreamListener):
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessSecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])





screen_name = sys.argv[1]

class MyException(Exception):
    pass


url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?' + screen_name + '=twitterapi'

try:
    user_feed = urllib2.urlopen(url, timeout = 1).read()
except urllib2.URLError as e:
    print 'Unable to connect to ' + screen_name + '\n'


