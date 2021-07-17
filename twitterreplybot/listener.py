
import tweepy
import time
import random
from twitterreplybot.replier import Replier

class Listener(tweepy.StreamListener):

    replier = None
    replies = []
    last_reply = -1
    api = None

    def __init__(self, replies, api):
        self.replies = replies
        self.api = api

    def on_status(self, tweet):
        author = tweet.author.screen_name
        tweet_id = tweet.id
        print(f"listened to {tweet.text} id = {tweet_id} from {author}")
        reply = self.get_reply()
        self.replier.reply(f'@{author} {reply}', tweet_id)

    def start_replier(self):
        self.replier = Replier(self.api)

    def get_reply(self):
        ind = random.randrange(0, len(self.replies))
        while ind == self.last_reply:
            ind = random.randrange(0, len(self.replies))
        self.last_ind = ind
        return self.replies[ind]