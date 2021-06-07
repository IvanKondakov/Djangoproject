import os
import requests
import sys
from dotenv import load_dotenv

load_dotenv()

def tel_bot():
    bot_api_key = os.getenv("BOT_API_KEY")
    channel_name = os.getenv("CHANNEL_NAME")
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
