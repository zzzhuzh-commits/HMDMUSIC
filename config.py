from pyrogram import Client, filters
from config import OWNER_ID


@Client.on_message(filters.text & filters.regex("^المطور$"))
async def owner_panel(_, message):

    if message.from_user.id != OWNER_ID:
        return

    await message.reply_text(
        """
👑 لوحة مطور HMDMUSIC

• الاحصائيات
• فحص
• اذاعة

🎵 HMDMUSIC
"""
    )


@Client.on_message(filters.text & filters.regex("^فحص$"))
async def ping_command(_, message):

    if message.from_user.id != OWNER_ID:
        return

    await message.reply_text(
        "✅ البوت يعمل بنجاح"
    )
