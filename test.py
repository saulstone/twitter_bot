obj = open("tweet.txt","r")

recent_tweets_id = []
recent_tweets_id = obj.readlines()
since_id = recent_tweets_id[0]

print(since_id)
