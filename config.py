import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    #these are the API key and secret required to get access to Twitter api methods
    #access key and secret is required to get access to the data of your own twitter account
    CONSUMER_KEY = 'xxxxxxxxxxxxxxxx'
    CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    ACCESS_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    ACCESS_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxx'

    #Authenication and creating the object to twitter api.
    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating api",exc_info=True)
        raise e
    logger.info("API created")
    return api
