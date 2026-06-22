from pyrogram import Client, filters
from HMDMUSIC.core.database import db

groupsdb = db.groups


@Client.on_message(filters.group)
async def save_groups(_, message):

    chat_id = message.chat.id

    data = await groupsdb.find_one(
        {"chat_id": chat_id}
    )

    if not data:
        await groupsdb.insert_one(
            {"chat_id": chat_id}
        )
