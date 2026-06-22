from pyrogram import Client, filters

from HMDMUSIC.core.queue import add_to_queue, get_queue

@Client.on_message(filters.text & filters.regex(r"^شغل (.+)"))
async def play_command(_, message):

    song = message.text[4:].strip()

    add_to_queue(
        message.chat.id,
        song
    )

    position = len(
        get_queue(message.chat.id)
    )

    await message.reply_text(
        f"🎵 تمت إضافة الأغنية\n\n"
        f"📌 {song}\n"
        f"📋 الترتيب: {position}"
    )
