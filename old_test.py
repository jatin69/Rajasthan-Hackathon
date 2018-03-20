import tweepy

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

import json
from textblob import TextBlob

def main():

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    #print("sucess")
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    #print("sucess")
    api = tweepy.API(auth)
    #print("sucess")

    # public_tweets = api.home_timeline()
    #print("sucess")

    query = "amberfort"
    public_tweets = api.search(query, count=1)

    fields = ['id', 'text', 'created_at', 'geo', 'coordinates', 'place', 'retweet_count',
              'favorite_count']

    tweet_dict = {}
    for tweet in public_tweets:
        print("ok")
        temp = dict()

        for field in fields:
            temp[str(field)] = eval('tweet' + '.' + str(field))

        # temp['text'] = tweet.text
        # temp['created_at'] = tweet.created_at

        tweet_dict[str(tweet.id)] = temp

    unique_tweets = {}

    for key, value in tweet_dict.items():
        if key not in unique_tweets.keys():
            unique_tweets[key] = value

    # print(unique_tweets)

    for key in unique_tweets:
        print(key)
        for value in unique_tweets[key]:
            print(value, ':', unique_tweets[key][value])
        print("--------------------------------------------------")

    # print(*unique_tweets, sep="\n")

    # print(tweets)
    # testimonial = TextBlob(tweets)
    # print(testimonial.sentiment)

    # query = "pinkcity"
    # for tweet_info in tweepy.Cursor(api.search, q=query, lang='en', tweet_mode='extended').items(5):
    #     # print(tweet_info)
    #     # print(tweet_info._json)
    #     tweet = ""
    #     if 'retweeted_status' in dir(tweet_info):
    #         tweet = tweet_info.retweeted_status.full_text
    #     else:
    #         tweet = tweet_info.full_text
    #     print(tweet)


if __name__ == '__main__':
    main()
