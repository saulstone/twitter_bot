#tweepy is the python library which contains the twitter api methods and classes.
#importing time to deal with real time functions like waiting,etc.
import tweepy
import time
import logging
from config import create_api
import os

def get_user_info():
    name = "narendramodi"
    user = api.get_user(name)
    #print(dir(user)
    print("Screen Name:",user.name)
    print("Location:",user.location)
    print("Twitter unique id:",user.id)
    print("Total followers:",user.followers_count)
    print("Total following count:",user.friends_count)
    #d={}
    #d=user.__dict__
    #print(d['name'])

    #getting tweets of a prticular a particular get_user
    #for status in tweepy.Cursor(api.user_timeline).items(1):
        #print(status)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api,since_id):
    logger.info("Retrieving the mentions")
    new_since_id=since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,since_id=new_since_id).items():
        new_since_id = max(tweet.id,new_since_id)
        if tweet.in_reply_to_status_id is not None:
            print(tweet.created_at)
            continue
        logger.info(f"Anserwing to {tweet.user.name}")
        status1 = "@"+str(tweet.author.screen_name)+" "+"Please reach me and team via DM"
        api.update_status(status=status1,in_reply_to_status_id=tweet.id)
    return new_since_id

def main():

    api = create_api()
    #since_id = 1172035803570032641
    while True:
        rr = open("tweet.txt","r")
        obj = open("tweet.txt","a+")
        recent_tweets_id = []
        recent_tweets_id = rr.readlines()
        since_id1 = recent_tweets_id[-1]

        print(since_id1)

        since_id = check_mentions(api,int(since_id1))
        if(int(since_id1)!=(since_id)):
            obj.write(str(since_id)+"\n")
        print(since_id)
        logger.info("Waiting....")
        rr.close()
        obj.close()
        time.sleep(3*60)
if __name__=="__main__":
    main()
