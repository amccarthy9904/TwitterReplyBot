
class Replier():

    api = None

    def __init__(self, api):
        self.api = api

    def reply(self, message, tweet_id):
        self.api.update_status(message, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)
        print(f"sent {message} in response to {tweet_id}")