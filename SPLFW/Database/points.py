from . import db

points = db.points

async def update_user_points(chat_id: int, user_id: int, points: int):
    y = await get_user_points(chat_id, user_id)
    points += y
    await points.update_one({"chat_id": chat_id}, {"$set": {"info": {user_id: points}}}, upsert=True)

async def get_user_points(chat_id: int, user_id: int):
    x = await points.find_one({"chat_id": chat_id})
    if not x:
        return 0
    return x["info"][user_id]
