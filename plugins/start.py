from pyrogram import filters
from pyrogram import Client

@Client.on_message(filters.text & filters.regex("^هلا$"))
async def start_message(_, message):
    await message.reply_text(
        "🎵 أهلاً بك في HMDMUSIC"
    )
