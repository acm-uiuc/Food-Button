import requests
from requests_oauthlib import OAuth1

# ASK Marcell For Keys
APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_SECRET = ''

auth = OAuth1(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_SECRET)

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
print(requests.get(url, auth=auth).json())

from twython import Twython

twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_SECRET)
with open('anakin-its-working-o.gif', 'rb') as f:

    twitter.update_status_with_media(media=f, status="It's Working!")
