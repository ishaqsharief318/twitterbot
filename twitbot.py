import tweepy
import sys
import time
import pickle
import ConfigParser
import logging

config = ConfigParser.ConfigParser()
config.read('secret.ini')

CONSUMER_KEY = config.get('keys', 'consumerkey')
CONSUMER_SECRET = config.get('keys', 'consumersecret')
ACCESS_KEY = config.get('keys', 'accesskey')
ACCESS_SECRET = config.get('keys', 'accesssecret')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


tweet_dict = {}

retwt_list = ["@ManUtdStuff","@ManUtd_Hindi","@juanmata8","@ManUtd"]

def make_file():
	try:
		for account in retwt_list:
			retwt = api.user_timeline(id = account, count = 1)
			for each in retwt:
				tweet_dict[account] = each.id
		with open('tweetdict.pickle', 'wb') as handle:
			pickle.dump(tweet_dict, handle)
	except Exception as e:
		print str(e)

def read_file():
	with open('tweetdict.pickle', 'rb') as handle:
		tweet_file = pickle.load(handle)

read_file()
