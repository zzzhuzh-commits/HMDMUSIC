from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def start_message(client, message):
    await message.reply_text(
        "🎵 أهلاً بك في HMDMUSIC"
    )
