from pyrogram import Client, filters 
from SPLFW.Database.limit import *

@Client.on_message(filters.command("change") & filters.group)
async def change(_, m):
    if len(m.command) != 2:
        return await m.reply("`/change (100-1000)`")
    try:
        value = int(m.text.split()[1])
    except:
        return await m.reply("`/change (100-1000)`")
    if (value < 100) or (value > 1000):
        return await m.reply("`/change (100-1000)`")
    x = await _.get_chat_member(m.chat.id, m.from_user.id)
    if not x.status.name in ["OWNER", "ADMINISTRATOR"]:
        return await m.reply("`Only group staff can change !`")
    y = await get_chat_limit(m.chat.id)
    await update_chat_limit(m.chat.id, value)
    await m.reply(f"`value has been changed from {y} to {value}.`")
