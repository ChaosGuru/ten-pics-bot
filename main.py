"""
Bot - t.me/TenPicsBot

Give you 10 reandom pictures based on your input text.
"""

import requests as rqs
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
from random import randint
import logging

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, I am bot. What do you want to see?')

def echo(update, context):
    # search link based on input text
    with open('googling.json') as f:
        apis = json.load(f)
    search_link = "https://customsearch.googleapis.com/customsearch/v1?cx={0}&imgSize=LARGE&num=10&q={1}&searchType=image&start={3}&key={2}".format(apis['cx'], update.message.text, apis['key'], randint(0, 5)*10 + 1)

    # search for images
    res = rqs.get(search_link)
    print(res.status_code)

    # get photos urls from response json
    photos = []
    search_photos = json.loads(res.text)
    for photo in search_photos["items"]:
        photos.append(telegram.InputMediaPhoto(media=photo["link"]))

    # send album of photos
    context.bot.send_media_group(chat_id=update.effective_chat.id, media=photos)

def main():
    # get tocken
    with open('token.json') as f:
        token = json.load(f)["token"]

    # logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # bot's updater and dispatcher
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    # command handler
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # message handler
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()