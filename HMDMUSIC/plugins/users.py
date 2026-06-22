from pyrogram import Client, filters
from HMDMUSIC.core.database import usersdb


@Client.on_message(filters.private)
async def save_users(_, message):

    user_id = message.from_user.id

    data = await usersdb.find_one(
        {"user_id": user_id}
    )

    if not data:
        await usersdb.insert_one(
            {"user_id": user_id}
        )
