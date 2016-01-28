import sys
import urllib2


screen_name = sys.argv[1]

url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?' + screen_name + '=twitterapi'


user_feed = urllib2.urlopen(url).read()
