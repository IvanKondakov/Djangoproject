#import os
import requests
import sys

def tel_bot():
    bot_api_key = "1802025375:AAH1e82nx7Elurv8XyExvF2YyngWPw9iKMs"
    channel_name = "@FortysixthBotDjango"
    message = sys.argv[1]

    url = f'https://api.telegram.org/bot{bot_api_key}/sendMessage'

    params = {
        'chat_id': channel_name,
        'text': message,
    }

    return requests.get(url, params=params).json()

tel_bot()
