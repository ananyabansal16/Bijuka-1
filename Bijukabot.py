"""
Simple Bot to reply to Telegram messages taken from the python-telegram-bot examples.
Source: https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py
"""

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
import requests
import cv2

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '5171667370:AAFaN1oDzj1qotI-XCsD4kw7ISOGo-HCssE'

latestBackNavigation = InlineKeyboardMarkup([[InlineKeyboardButton(
    "« Back", callback_data='latest'), InlineKeyboardButton("✗ Exit", callback_data='exit')]])
trendBackNavigation = InlineKeyboardMarkup([[InlineKeyboardButton(
    "« Back", callback_data='trend'), InlineKeyboardButton("✗ Exit", callback_data='exit')]])

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def Start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Welcome to Bijuka. Please select you language. Enter /English for English, /Hindi for Hindi and /Punjabi for Punjabi.\n\nनमस्ते! बीजूका में आपका स्वागत है। कृपया अपनी भाषा चुनें। अंग्रेजी के लिए /English, हिंदी के लिए /Hindi और पंजाबी के लिए /Punjabi दर्ज करें।\n\nਹੈਲੋ! ਬੀਜੂਕਾ ਵਿੱਚ ਤੁਹਾਡਾ ਸੁਆਗਤ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਆਪਣੀ ਭਾਸ਼ਾ ਚੁਣੋ। ਅੰਗਰੇਜ਼ੀ ਲਈ /English, /Hindi ਲਈ ਹਿੰਦੀ ਅਤੇ ਪੰਜਾਬੀ ਲਈ /Punjabi ਦਰਜ ਕਰੋ।')

def English(update, context):
    update.message.reply_text('Use /Image command to identify the disease your rice crop has so that you can do the applicable treatment for you crop. Enter /Image and then enter the picture of affected crop.')

def Hindi(update, context):
    update.message.reply_text('अपनी धान की फसल में रोग की पहचान करने के लिए /Image कमांड का प्रयोग करें ताकि आप अपनी फसल के लिए उपयुक्त उपचार कर सकें। /Image दर्ज करें और फिर प्रभावित फसल की तस्वीर दर्ज करें।')

def Punjabi(update, context):
    update.message.reply_text('ਤੁਹਾਡੀ ਚੌਲਾਂ ਦੀ ਫਸਲ ਨੂੰ ਬਿਮਾਰੀ ਦੀ ਪਛਾਣ ਕਰਨ ਲਈ /Image ਕਮਾਂਡ ਦੀ ਵਰਤੋਂ ਕਰੋ ਤਾਂ ਜੋ ਤੁਸੀਂ ਆਪਣੀ ਫਸਲ ਲਈ ਲਾਗੂ ਇਲਾਜ ਕਰ ਸਕੋ। /Image ਦਰਜ ਕਰੋ ਅਤੇ ਫਿਰ ਪ੍ਰਭਾਵਿਤ ਫਸਲ ਦੀ ਤਸਵੀਰ ਦਰਜ ਕਰੋ।')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('/start \n/help\n/helpline' )
    
def helpline(update, context):
    "displays farmers helpline numbers"
    update.message.reply_text('9998887623 9988776655')

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

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("Start", Start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("helpline",helpline))
    dp.add_handler(CommandHandler("English",English))
    dp.add_handler(CommandHandler("Hindi",Hindi))
    dp.add_handler(CommandHandler("Punjabi",Punjabi))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)
    updater.start_polling()
    #updater.bot.setWebhook("https://bijuka.herokuapp.com/" + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
    # Start the Bot
   