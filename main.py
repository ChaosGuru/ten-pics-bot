"""
Bot - t.me/TenPicsBot

Give you 10 reandom pictures based on your input text.
"""

import requests as rqs
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="F***ing freak, what i need to find this time!!?")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main():
    # get tocken
    with open('token.json') as f:
        token = json.load(f)["token"]

    # set logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # get updater and dispatcher
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    # set command handler
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # set message handler
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # start the bot
    updater.start_polling()

if __name__ == '__main__':
    main()