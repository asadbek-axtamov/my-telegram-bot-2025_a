# Get toke from the environment variable
import os
from telegram import Bot
token = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = Bot(token)
CHAT_ID = 7157297566


document = 'asdf.ogg'
response = bot.send_voice(CHAT_ID, document)
print(response)