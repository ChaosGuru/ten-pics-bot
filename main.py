"""
Bot - t.me/TenPicsBot

Give you 10 reandom pictures based on your input text.
"""

import requests as rqs
import telegram
import json

# class Bot:
#     def __init__(self, token):
#         self.bot = r'https://api.telegram.org/bot' + token

#     def getMe(self):
#         response = rqs.get(self.bot + '/getMe').text
#         return json.loads(response)

def main():
    # get tocken
    with open('token.json') as f:
        token = json.load(f)["token"]

    # get bot
    bot = telegram.Bot(token=token)
    print(bot.get_me())

    # TenPicsBot = Bot(token)
    # print(TenPicsBot.getMe())

if __name__ == '__main__':
    main()