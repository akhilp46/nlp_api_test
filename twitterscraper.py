from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta, timezone

def get_tweets(target_account):
    #get relevant authentication keys from local text files
    consumer_key = open('twitter_consumer_key.txt').readline()
    consumer_secret = open('twitter_consumer_secret.txt').readline()
    access_token = open('twtter_access_token.txt').readline()
    access_token_secret = open('twitter_access_token_secret.txt').readline()

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    auth_api = API(auth)

    # #twitter account and description
    # target_account = "jaden"

    print("Getting data for " + target_account)
    item = auth_api.get_user(screen_name=target_account)
    print("name: " + item.name)
    print("screen_name: " + item.screen_name)
    print("description: " + item.description)
    print("statuses_count: " + str(item.statuses_count))
    print("friends_count: " + str(item.friends_count))
    print("followers_count: " + str(item.followers_count) + "\n")

    #iterate through set no. of tweets 
    tweet_list = []
    tweet_count = 0
    max_tweets = 20
    end_date = datetime.now(timezone.utc) - timedelta(days=5)

    for status in Cursor(auth_api.user_timeline, id=target_account).items():
        tweet_count += 1
        tweet_list.append(status.text)
        print("Tweet #" + str(tweet_count))
        print(tweet_list[tweet_count-1] + ": \n")
        
        if status.created_at < end_date:
            break
        if tweet_count >= max_tweets:
            break
        
    # print(tweet_list)
    return tweet_list