from pyrogram import Client
import time
from SPLFW.Database.limit import get_chat_limit

XD = {}
info = {}
@Client.on_message(group=1)
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
    if await get_chat_limit(m.chat.id) != XD[m.chat.id]:
        return
    XD[m.chat.id] = 0
    
    
