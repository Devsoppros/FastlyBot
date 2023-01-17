from pyrogram import Client, filters, idle
from config import *

yashu = Client(":SPLFW:", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="SPLFW"))

yashu.start()
print("Bot Started !")
idle()
