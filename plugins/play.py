from pyrogram import Client, filters

@Client.on_message(filters.text & filters.regex(r"^شغل (.+)"))
async def play_command(_, message):
    song = message.text[4:].strip()

    await message.reply_text(
        f"🎵 جاري البحث عن:\n\n{song}"
    )
