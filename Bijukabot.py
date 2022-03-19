"""
Simple Bot to reply to Telegram messages taken from the python-telegram-bot examples.

Source: https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py
"""

#from curses.panel import update_panels
import logging
import cv2
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, replykeyboardremove
from telegram.ext import updater, commandhandler, messagehandler, filters, callbackqueryhandler, conversationhandler, callbackcontext
from telegram.bot import log
import requests
x = requests.get("https://hacktoberfestapi.servatom.com/")
print(x.text)
import os

PORT = int(os.environ.get('PORT', 80))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '5171667370:AAFaN1oDzj1qotI-XCsD4kw7ISOGo-HCssE'

latestBackNavigation = InlineKeyboardMarkup([[InlineKeyboardButton( "« Back", callback_data='latest'), InlineKeyboardButton("✗ Exit", callback_data='exit')]])
trendBackNavigation = InlineKeyboardMarkup([[InlineKeyboardButton( "« Back", callback_data='trend'), InlineKeyboardButton("✗ Exit", callback_data='exit')]])

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update,       ):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')
    
def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

def image(update, context):
    update.message.photo[-1].get_file().download("img.jpg")
    
    img = cv2.imread()


    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    #updater.bot.setWebhook("https://bijuka.herokuapp.com/" + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()