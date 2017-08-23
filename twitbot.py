# -*- coding: utf-8 -*-
# flake8: noqa
#

import tweepy
import ConfigParser
import logging
import sys

config = ConfigParser.ConfigParser()
config.read('secret.ini')

CONSUMER_KEY = config.get('keys', 'consumerkey')
CONSUMER_SECRET = config.get('keys', 'consumersecret')
ACCESS_KEY = config.get('keys', 'accesskey')
ACCESS_SECRET = config.get('keys', 'accesssecret')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


retwt_list = ["@OptaJoe", "@ManUtd_Hindi", "@juanmata8", "@ManUtd", "@Redcafe", "@samuelluckhurst", "@FantasyScout1"]
keywords = ['Manchester United', 'mufc', '#mufc', '#manutd', 'manutd', 'José', 'Mourinho', 'josé', 'mourinho', 'Jose', 'Jose Mourinho' ]

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s:%(funcName)s:%(lineno)d - %(message)s', '%Y-%m-%d-%H:%M:%S'  # NOQA
))
logging.getLogger().setLevel(logging.INFO)
logging.getLogger().addHandler(handler)
log = logging.getLogger(__name__)

def rt_the_twts(retwt_list):
  for account in retwt_list:
    retwt = api.user_timeline(id=account, count=1)
    for each in retwt:
      try:
        log.info('Retweeting {} from {}'.format(api.retweet(each.text), account))
        api.retweet(each.id)
      except tweepy.error.TweepError:
        log.error('Already Tweeted')


rt_the_twts(retwt_list)
