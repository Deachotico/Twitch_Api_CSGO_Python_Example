# CSGOTwitchBot
Python BOT for Telgram that uses Twitch API to find streams in the Twitch.tv and send a notification via Telgram or by email if there is some stream with the given parameters.

### Deploy with virtualEnv

Make a virtualEnv using TwitchBot folder

`virtualenv venvTwitchBot`

Activate the VirtualEnv

`source venvTwitchBot/bin/activate`

Install the dependencies

`python Setup.py install`

if it fails run

`pip install python-telegram-bot`

Run bot

`python3 twitchbot.py`


### Twitch client id

To use it you need to generate a **Twitch Client-ID**, tutorial is in https://dev.twitch.tv/get-started
Put it in the code the `CSGOWatcher.py` file here:

  `eq.add_header("Client-ID","PUT_IT_HERE")`

To use it with other games you can change the parameters sent in the url with other games or options, reference here: https://dev.twitch.tv/docs/v5/reference/streams

### Telegram Bot Setup

To use the Telegram Bot you will need to create one talking with https://telegram.me/botfather, **he will generate a token**, you need to put it in the `twitchbot.py` here:

`updater = Updater("PUT_TOKEN_HERE")`

### Gmail setup

Your gmail personal password will not work.
To send the email using a Gmail Account you need a app password, tutorial to generate one is in here:
https://support.google.com/accounts/answer/185833?hl=en
You pass it to the `send_email` function as the **pwd parameter**.

Change this line in twitchbot.py with the required parameters
` send_email('put_youremail_here' ,'Put your app password here', ['put your destination emails here'],
                       'CSGO New Livestreams at Twitch', body) `

### Files structure

**twitchbot.py** - Telegram Bot and his configs.

**CSGOWatcher.py** - Script that get streams data form Twitch Api.

**emailmodule.py** - Module that send a email if requested using Gmail.