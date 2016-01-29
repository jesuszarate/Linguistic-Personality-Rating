import sys
import urllib2


screen_name = sys.argv[1]

class MyException(Exception):
    pass


url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?' + screen_name + '=twitterapi'

try:
    user_feed = urllib2.urlopen(url, timeout = 1).read()
except urllib2.URLError as e:
    print 'Unable to connect to ' + screen_name + '\n'


