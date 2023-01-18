from pyrogram import Client, filters, idle
from config import *
from SPLFW import load_bg, load_words

yashu = Client(":SPLFW:", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="SPLFW"))

load_words()
load_bg()
yashu.start()
print("Bot Started !")
idle()
