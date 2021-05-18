#import os
import requests
import sys

def tel_bot():
    bot_api_key = "1802025375:AAHeXYACoOhregUc9q3NrdgYzxOVrigIkcE"
    channel_name = "@FortysixthBotDjango"
    message = sys.argv[1]

    url = f'https://api.telegram.org/bot{bot_api_key}/sendMessage'

    params = {
        'chat_id': channel_name,
        'text': message,
        'disable_web_page_preview': True,
        'parse_mode': "markdown",
    }

    return requests.post(url, params=params).json()

tel_bot()
