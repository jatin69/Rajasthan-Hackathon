import tweepy
import re
import pandas as pd

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

def main():
    # Authenticate
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # unique_tweets = {}
    #
    # for key, value in tweet_dict.items():
    #     if key not in unique_tweets.keys():
    #         unique_tweets[key] = value
    #
    # # print(unique_tweets)
    #
    # for key in unique_tweets:
    #     print(key)
    #     for value in unique_tweets[key]:
    #         print(value, ':', unique_tweets[key][value])
    #     print("--------------------------------------------------")
    #
    # # print(*unique_tweets, sep="\n")
    #
    # # print(tweets)
    # # testimonial = TextBlob(tweets)
    # # print(testimonial.sentiment)

    # query = "pinkcity"
    keywords = ['id', 'text', 'created_at', 'geo', 'coordinates', 'place', 'retweet_count', 'favorite_count']

    queries = ['jaisalmerfort', 'amberfort', 'nahargarhfort', 'karnimatafair',
               'ohmyrajasthan', 'rangsthan', 'jaanekyadikhjaaye', 'my_rajasthan',
               'amerfort', 'mountabu'
               ]
    # # queries = [ 'jaipur' ]
    tweets = {}
    # searchTerms = "mountabu"
    # for query in queries:
    #     searchTerms += " OR " + query
    #
    # print(searchTerms)
    #

    # replace here all one by one
    searchTerms = 'my_rajasthan'
    print(searchTerms)

    for tweet_info in tweepy.Cursor(api.search, q=searchTerms, lang='en', tweet_mode='extended').items(100):
        print("ook")
        # print("cool")
        # print(dir(tweet_info))
        # print(tweet_info._json)
        fullTweet = ""
        if 'retweeted_status' in dir(tweet_info):
            fullTweet = tweet_info.retweeted_status.full_text
        else:
            fullTweet = tweet_info.full_text

        filtered_tweet = fullTweet
       # filtered_tweet = re.sub(r"http\S+", "", fullTweet)
        key = tweet_info.id_str
        value = {
            'id': tweet_info.id_str,
            'text': filtered_tweet,
            'created_at': tweet_info.created_at,
            'retweet_count': tweet_info.retweet_count,
            'favorites_count': tweet_info.favorite_count
        }
        tweets[key] = value

    print("============================================")
    # print(tweets)

    unique_tweets = {}

    for key, value in tweets.items():
        if key not in unique_tweets.keys():
            unique_tweets[key] = value

    # print(unique_tweets)
    #
    for key in unique_tweets:
        print(key)
        for value in unique_tweets[key]:
            print(value, ':', unique_tweets[key][value])
        print("--------------------------------------------------")

    df = pd.DataFrame(unique_tweets).T
    # print(df)
    # df.id = df.id.astype(str)
    with open('text.csv', 'a') as f:
        df.to_csv(f, header=False)


if __name__ == '__main__':
    main()
