import tweepy

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
               'amerfort', 'mountabu',
               ]
    # queries = [ 'jaipur' ]
    tweets = {}

    print("ok")
    query = "my_rajasthan"
    for tweet_info in tweepy.Cursor(api.search, q=query, lang='en', tweet_mode='extended',
                                    result_type='popular').items(5):
        print("cool")
        # print(dir(tweet_info))
        # print(tweet_info._json)
        fullTweet = ""
        if 'retweeted_status' in dir(tweet_info):
            fullTweet = tweet_info.retweeted_status.full_text
        else:
            fullTweet = tweet_info.full_text

        key = tweet_info.id_str
        value = {
            'id': tweet_info.id,
            'text': fullTweet,
            'created_at': tweet_info.created_at,
            'place': tweet_info.place,
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

    for key in unique_tweets:
        print(key)
        for value in unique_tweets[key]:
            print(value, ':', unique_tweets[key][value])
        print("--------------------------------------------------")


if __name__ == '__main__':
    main()
