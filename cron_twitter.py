import pandas as pd
from apscheduler.schedulers.blocking import BlockingScheduler
import tweepy
from tweepy import OAuthHandler
import json

# Authentication credential
consumer_key = "nB0eGW0EAU7CmIpUKxLU4zJlk"
consumer_secret = "fAOmc2l2VrHJrSpAOkjMrbqUOyK4LtqxDgkJt3SWFgJ7Xv9xXN"
access_token = "115400505-T5aMAjmG689yM9bM2BYeQqG56Yd1mk2qUn5zJoMv"
access_secret = "P4CSlEFiMz9DUiyDm7KvALwmKYjzTj247dpbW3VppnA4G"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
auth_api = tweepy.API(auth)

# Pass twitter ID to mine data
# target_list = []
target_id = "EPA_Victoria"

# Getting data from user
item = auth_api.get_user(target_id)
#json_store(item._json)



# Auxiliary functions
# Get latest tweet
def get_last_tweet(id):
    tweet = auth_api.user_timeline(id=id, count = 5)
    json_store(tweet[0]._json)

# Store as JSON
def json_store(data):
    with open('status.json','a+') as outfile:
        json.dump(data, outfile)

get_last_tweet(target_id)


# Scheduler to run every morning at 8am
# 8AM is the time EPA and MelbournePollen posts Tweet forecast
# sched = BlockingScheduler()
#
# @sched.scheduled_job('cron', day_of_week = 'mon-sun', hour = 8)
# def extract_twitter():
#     print('pollen level is: ')#
#
#
# sched.start()