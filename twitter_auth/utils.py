import tweepy

CONSUMER_KEY = '3dYGecJ90843FNVDz3JNjHHmU'
CONSUMER_SECRET = '2zK0VY7f53AJaEo6Rpc1XdtrJqnO7vxroFwQRDh6uPEkiSE2NQ'

def get_api(request):
# set up and return a twitter api object
  oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  access_key = request.session['access_key_tw']
  access_secret = request.session['access_secret_tw']
  oauth.set_access_token(access_key, access_secret)
  api = tweepy.API(oauth)
  return api
