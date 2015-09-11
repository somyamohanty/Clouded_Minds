'''
Tweet Collector, Stores them in mongodb.

'''


import sys
import tweepy
import json
import pymongo
import time
from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener

client = pymongo.MongoClient('localhost', 27017)
db = client.test

consumer_key="49Bm94064sFbIAUc6s5sNw"
consumer_secret="oOasOsaSm9g3IiYhmn0IEMiwwwHqU8BChckpAlKRg"

access_token="123009309-gfMe9KZT1FGYgDokOajYA1SRWBInX4F0gkFP4PXL"
access_token_secret="KZvfQqLijN5rtMd836YsHRJMgqOaJUbF06t7KQpf4rxLa"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

config={}
with open('config.txt','r') as configfile:
	for line in configfile:
		if line.startswith('#'):
			continue
		name,var=line.partition('=')[::2]
		config[name.strip()]=var.strip()

#end_time=1442082600
end_time=1441944660
start_time=int(config['starttime']) if config['starttime'] else time.time()

end_time=int(config['endtime'])
keywords=config['keywords'].split(',')

class TweetListener(StreamListener):
  def __init__(self, api):
    self.api = api
    super(tweepy.StreamListener, self).__init__()
    self.db = pymongo.MongoClient()[config['db']]

  def on_status(self, tweet):
    data = {}
    data['text'] = tweet.text
    data['user'] = tweet.user.screen_name
    data['timestamp'] = tweet.timestamp_ms
    data['created_at'] = tweet.created_at
    data['geo'] = tweet.geo
    data['lang'] = tweet.lang
    
    #Store only 'non-retweeted' tweets.
    if not tweet.retweeted and 'RT @' not in tweet.text: 
    	print data, '\n', tweet.retweeted
	self.db.Tweets.insert(data)
	if time.time() > end_time:
		print 'Time Finished'
		return False

  def on_error(self, status):
    print >> sys.stderr, 'Error: ', status
    return True

  def on_timeout(self):
    print >> sys.stderr, 'Stream timeout'
    return True

#Sleep Till Start Time is reached.
sleeptime = start_time-time.time() if (start_time-time.time()) > 1 else 0
time.sleep(sleeptime)
#Start Streaming
listen = Stream(auth, TweetListener(api))
listen.filter(track=keywords)
