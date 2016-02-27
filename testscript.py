import tweepy
import sys
import time
import pickle
import os.path

CONSUMER_KEY = 'dJSc6Jc2rQ0bDAyh6zBBeX980'
CONSUMER_SECRET = 'KMUqE9HcDJ6PyNUJFVbYKlkJfgqE7DdAIgaarrfuVs0UkTL3zL'
ACCESS_KEY = '1086665743-1UhEDYJHzNR61LZ6qXbAcSKAb63l5TZpNzCAjVC'
ACCESS_SECRET = '10HEYkOneRVXlQQE1t7VVPBU7SNjhZ5rDsBDdHXUF3E6G'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


tweet_dict = {}

retwt_list = ["@ManUtdStuff","@ManUtd_Hindi","@juanmata8","@ManUtd"]
for account in retwt_list:
	retwt = api.user_timeline(id = account, count = 1)
	for each in retwt:
		tweet_dict[account] = (each.id , each.text.encode('ascii','ignore'))
print tweet_dict

