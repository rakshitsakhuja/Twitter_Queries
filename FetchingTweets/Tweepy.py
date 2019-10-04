import os
import tweepy as tw
import pandas as pd
import sys
import csv
import time

consumer_key=''
consumer_secret=''
#access_token=''
#access_token_secret=''

auth = tw.AppAuthHandler(consumer_key, consumer_secret)
api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

Keyword_search = "TV OR smarttv AND smart"
new_search= Keyword_search+"-filter:retweets"

df=pd.DataFrame()

k=0
a=[]
for tweet in tw.Cursor(api.search,q=new_search,lang="en",since='2019-09-17', tweet_mode='extended').items():
#     print (tweet.created_at, tweet.text, tweet.user.screen_name, tweet.user.location)
    b=[tweet.created_at, tweet.full_text, tweet.user.screen_name, tweet.user.location, tweet.retweet_count, tweet.favorite_count]
    a.append(b)
    k+=1
    print(k)
    if k%1000==0:
        abc=pd.DataFrame(a)
        abc.columns=['tweet.created_at', 'tweet.full_text', 'tweet.user.screen_name', 'tweet.user.location', 'tweet.retweet_count', 'tweet.favorite_count']
        abc.to_csv('20190927_v6.csv',index=False,encoding='utf8')

pd.DataFrame(a)

abc=pd.DataFrame(a)
abc.columns=['tweet.created_at', 'tweet.full_text', 'tweet.user.screen_name', 'tweet.user.location', 'tweet.retweet_count', 'tweet.favorite_count']
abc.to_csv('20190927.csv',index=False,encoding='utf8')
