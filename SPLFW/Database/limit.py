from . import db

limit = db.limit

async def update_chat_limit(chat_id: int, value: int):
    await limit.update_one({"chat_id": chat_id}, {"$set": {"limit": value}}, upsert=True)

async def get_chat_limit(chat_id: int):
    x = await limit.find_one({"chat_id": chat_id})
    if not x:
        return 100
    return x["limit"]
