from pyrogram import Client
import time
from SPLFW.Database.limit import get_chat_limit

XD = {}
a = 0
@Client.on_message(group=1)
async def cwf1(_, m):
    global XD, a
    if not m.from_user:
        return
    if not m.from_user.id:
        return
    a += 1
    XD[m.chat.id] = a
    if await get_chat_limit(m.chat.id) != a:
        return
    a = 0
    
