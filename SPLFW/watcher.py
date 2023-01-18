from pyrogram import Client, filters
import time
from SPLFW.Database.limit import get_chat_limit
from . import WORDS
import random
from .paste import create_image

XD = {}
info = {}
@Client.on_message(filters.group, group=1)
async def cwf1(_, m):
    global XD, info
    if not m.from_user:
        return
    if not m.from_user.id:
        return
    if not m.chat.id in XD:
        XD[m.chat.id] = 1
    else:
        XD[m.chat.id] += 1
    if 10 != XD[m.chat.id]:
        return
    XD[m.chat.id] = 0
    text = random.choice(WORDS)
    img = create_image(text)
    info[m.chat.id] = [True, text]
    await _.send_photo(img, caption="Write the word !")

@Client.on_message(filters.group, group=2)
async def cwf2(_, m):
    global info
    if not m.chat.id in info:
        return
    if not info[m.chat.id][0]:
        return
    if len(m.command) != 1:
        return
    if m.text.lower() != info[m.chat.id][1].lower():
        return
    info[m.chat.id] = [False, None]
    await m.reply("First !")
    
    
