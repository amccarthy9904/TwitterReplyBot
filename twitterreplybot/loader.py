
import fileinput
import re
import random

class Loader():

    secret_pocket = []
    account_pocket = []
    message_pocket = []

    def __init__(self):
        self.fill_pocket(self.secret_pocket, 'secrets.txt')
        self.fill_pocket(self.account_pocket, 'accounts.txt')
        self.fill_pocket(self.message_pocket, 'messages.txt')


    def fill_pocket(self, pocket, filename):
        with fileinput.input(files=filename) as f:
            for line in f:
                m = re.search(r'[%#]', line)
                if not m and line.strip():
                    pocket.append(line.strip())

    
    def get_secret(self, ind):
        """Returns a specific secret"""
        return self.secret_pocket[ind]
    
    def get_accounts(self):
        """Returns all accounts"""
        return self.account_pocket
    
    def get_messages(self):
        """Returns all messages"""
        return self.message_pocket