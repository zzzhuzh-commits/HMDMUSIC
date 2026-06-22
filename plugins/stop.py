from pyrogram import Client, filters

@Client.on_message(filters.text & filters.regex("^ايقاف$"))
async def stop_command(_, message):
    await message.reply_text(
        "⏹ تم إيقاف التشغيل"
    )
