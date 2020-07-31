import tweepy
import json
from datetime import datetime, date, time, timedelta,timezone
from collections import Counter

def twittercollector(id, begintime, endtime):

    consumer_key = "q3tv2FEcuhreRWO4WYtSAyJAj"
    consumer_secret = "vxrXdz8TpiQQhQv7GSHMBliGQoMzGPNMdUpcVercmCYb8UqvzF"
    access_token = "1106978050850328578-2HjYKtDlRU3J88emRjV4TmkUapeJWl"
    access_token_secret = "doG0kjyHoD4tGBUnKTneUDZjUD392dRR3z8PwTJ2Autwm"


    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    auth_api = tweepy.API(auth)

    target= id

    beginday = begintime
    endday = endtime
    beginday_datetime_string = beginday + " 00:00:00"  
    endday_datetime_string = endday + " 23:59:59"  


    beginday_datetime = datetime.strptime(beginday_datetime_string,'%Y%m%d %H:%M:%S')
    endday_datetime = datetime.strptime(endday_datetime_string,'%Y%m%d %H:%M:%S')

    beginday_datetime_germany = beginday_datetime.replace(tzinfo=timezone(timedelta(hours=1))) 
    endday_datetime_germany = endday_datetime.replace(tzinfo=timezone(timedelta(hours=1)))
    beginday_datetime_utc = beginday_datetime_germany.astimezone(timezone.utc) 
    endday_datetime_utc = endday_datetime_germany.astimezone(timezone.utc) 

    beginday_datetime_utc = beginday_datetime_utc.replace(tzinfo=None) 
    endday_datetime_utc = endday_datetime_utc.replace(tzinfo=None) 


    tweets = []
    for tweet in tweepy.Cursor(auth_api.user_timeline,id=target,tweet_mode="extended").items():
    
        if tweet.created_at >= beginday_datetime_utc and tweet.created_at <= endday_datetime_utc :
            tweets.append(tweet._json)
            
    print(tweets)
    return tweets

if __name__ == "__main__":
    id = 'egrefen'
    begintime = "20200101"
    endtime = "20200131"
    twittercollector(id, begintime, endtime)