from pyrogram import Client, filters

@Client.on_message(filters.text & filters.regex("^تخطي$"))
async def skip_command(_, message):
    await message.reply_text(
        "⏭ تم تخطي الأغنية"
    )
