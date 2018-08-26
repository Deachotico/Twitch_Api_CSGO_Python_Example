#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:

Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from CSGOWatcher import CSGOWatcher

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')
    help(bot, update)

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('''COMANDS:\n/CSGO - CSGO Topstreams\n/LOL - LOL Topstreams\n
    /Fortnite - Fortnite Topstreams\n/PUBG - PUBG Topstreams\n/Dota - Dota Topstreams
    /Overwatch - Overwatch Topstreams\n/Heartstone - Heartstone Topstreams\n/FIFA - FIFA Topstreams
    \n/TOP - Top streams of any game''')

#Game functions
def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text("See /help man")

def getgame(bot, update):
    '''
    Call the function that handle twitch querys and return streams

    :return: update the user chat with the streams asked by him
    '''
    game = update.message.text.replace("/", "").lower()
    games = ["csgo", "lol", "fortnite", "pubg", "dota", "overwatch", "heartstone", "fifa", "top"]
    Return = CSGOWatcher(games.index(game))
    for stream in Return:
        update.message.reply_text(stream)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("<PUT_TOKEN_HERE>")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # answer in telegram for each command
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("csgo", getgame))
    dp.add_handler(CommandHandler("lol", getgame))
    dp.add_handler(CommandHandler("fortnite", getgame))
    dp.add_handler(CommandHandler("pubg", getgame))
    dp.add_handler(CommandHandler("dota", getgame))
    dp.add_handler(CommandHandler("overwatch", getgame))
    dp.add_handler(CommandHandler("heartstone", getgame))
    dp.add_handler(CommandHandler("fifa", getgame))
    dp.add_handler(CommandHandler("top", getgame))
    
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()