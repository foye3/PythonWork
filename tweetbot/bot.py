import tweepy
from secrets import *

#create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

auth.set_access_token(access_token, access_secret)

 #Construct the API instance
api = tweepy.API(auth) # create an API object

#read tweets from timeline
'''
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
'''
#get all your followers
'''
user = api.get_user('Fan07619587')
for friend in user.friends():
   print(friend.screen_name)
'''