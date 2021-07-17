
# Twitter Reply Bot

#### Development Version: v0.1.

This is a bot that replies to a given list of twitter accounts.
Every time an account on the list tweets yout account will respond with a message.
Accounts are parsed from accounts.txt and messages from messages.txt.
The message that you respond with is chosen randomly at runtime.

This library is simple, easy-to-use, and reliable to keep the replies flowing.

## Pre-Install Setup

You will need a developer twitter account. [link](https://developer.twitter.com/en/apply-for-access)

## Installation

Pretty straightforward. I have attached detailed instructions below that should help you get started. 

#### NOTE: If `python` does not work, please try `python3`.

1. Download and Install Python 3.7 or higher: https://www.python.org/
2. `git clone` this repo or download it.
3. Open CommandPrompt / PowerShell / Terminal and `cd` into the main library folder.
   * Example: `cd C:\Users\Swar\Documents\TwitterReplyBot`
4. Create a virtual environment for Python. This is recommended if you use Python for other things.
	1. Create a new python environment: `python -m venv venv`
	   * The second `venv` can be renamed to whatever you want. I prefer `venv` because it's a standard.
	2. Activate the virtual environment. This must be done *every single time* you open a new terminal.
	   * Example Windows: `venv\Scripts\activate`
	   * Example Linux: `. ./venv/bin/activate` or `source ./venv/bin/activate`
	3. Confirm that it has activated by seeing the `(venv)` prefix. The prefix will change depending on what you named it.
5. Install the required modules: `pip install -r requirements.txt`
6. Get all the required keys from Twitter and paste them into secrets.txt.
7. Store a list of accounts to reply to in accounts.txt.
8. Write out the messages you want to reply with in messages.txt.
9. Run the bot: `python replybot`
   * or `python bin/replybot.py`

## Sponsor / Support this Library

This library took time and effort in order to create it. Consider sponsoring or supporting the library.

* XCH Address: xch1pz5adm6r9gz4hxs4n9gts6mg8yun25r0el6ddta6zjjp5n0npuasqrspnc
* ETH Address: 0x59071a9635d9a7584ea221b776437ed477015226
* BTC Address: 3JtrYr9J293sVJzTwxRqwvcH9KHoiraf1W
 
Credit to [Swar](https://github.com/swar/Swar-Chia-Plot-Manager) I used his README as a template for this one