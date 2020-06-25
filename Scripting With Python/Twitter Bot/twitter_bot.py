# Tweepy Documentation: http://docs.tweepy.org/en/latest/

import tweepy

# You can find consumer_key and consumer_secrets in your corresponding application in your Twitter developer account
# API key is your consumer_key
# API secret key is your consumer_secret

auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
  try:
    while True:
      yield cursor.next()
  except tweepy.RateLimitError:
    time.sleep(1000)


for follower in limit_handler(tweepy.Cursor(api.followers).items()):
  print(follower.name)
