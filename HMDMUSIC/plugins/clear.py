from pyrogram import Client, filters

from HMDMUSIC.core.queue import clear_queue

@Client.on_message(filters.text & filters.regex("^مسح القائمة$"))
async def clear_command(_, message):

    clear_queue(message.chat.id)

    await message.reply_text(
        "🗑 تم مسح القائمة"
    )
