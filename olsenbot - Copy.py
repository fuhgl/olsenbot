import tweepy
import random
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

par = open('olsen.txt').read().split('\n\n')
api.update_status(random.choice(par))

