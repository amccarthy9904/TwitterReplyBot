import tweepy
import time
from twitterreplybot.listener import Listener
from twitterreplybot.loader import Loader
from datetime import datetime


def start():
    loader = Loader()

    api_key = loader.get_secret(0)
    api_secret_key = loader.get_secret(1)
    b_token = loader.get_secret(2)
    access_token = loader.get_secret(3) 
    access_token_secret = loader.get_secret(4)

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    for account in loader.get_accounts():

        acct_id = str(api.get_user(account).id)
        acct_listener = Listener(loader.get_messages(), api)
        acct_listener.start_replier()
        acct_stream = tweepy.Stream(auth=api.auth, listener=acct_listener)
        acct_stream.filter(follow=[acct_id], is_async=True)

    while True:
        print(f'{datetime.now()} listening to accounts:')
        for l in loader.get_accounts():
            print(f'\t{l}')
        
        time.sleep(300)

