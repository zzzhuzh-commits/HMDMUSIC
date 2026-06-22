from pyrogram import Client, filters

from HMDMUSIC.core.queue import get_queue

@Client.on_message(filters.text & filters.regex("^القائمة$"))
async def queue_command(_, message):

    queue = get_queue(message.chat.id)

    if not queue:
        return await message.reply_text(
            "📭 القائمة فارغة"
        )

    text = "📋 قائمة التشغيل\n\n"

    for num, song in enumerate(queue, start=1):
        text += f"{num}. {song}\n"

    await message.reply_text(text)
