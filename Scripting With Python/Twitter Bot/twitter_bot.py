# Tweepy Documentation: http://docs.tweepy.org/en/latest/

import tweepy
import time

# You can find consumer_key and consumer_secrets in your corresponding application in your Twitter developer account
# API key is your consumer_key
# API secret key is your consumer_secret

auth = tweepy.OAuthHandler('pgvnIjVONosLflwCY6jBJAKSi', 'xYriAqG7496QmgnjAnKouaoHNMt83ndJKPeyq0B4KFDGo6QC6I')
auth.set_access_token('958956089893994496-Z9qpGpRjgXftcJ3aDkUBPhiIz7kXf1E', 'J8YTjiMf4RGFtLp1EcAjtKdyVGSEDIOj74buVaRdqAPP3')

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
    except StopIteration:
        return


for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    print(follower.name)

search_string = 'python'
numberOfTweets = 2
for tweet in limit_handler(tweepy.Cursor(api.search, search_string).items(numberOfTweets)):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as err:
        print(err.reason)
    except StopIteration:
        break