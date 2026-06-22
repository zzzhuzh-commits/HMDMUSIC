from pyrogram import filters
from pyrogram import Client

@Client.on_message(filters.text & filters.regex("^مساعدة$"))
async def help_message(_, message):
    await message.reply_text(
        """
🎵 أوامر HMDMUSIC

• شغل
• تخطي
• ايقاف
• استئناف
        """
    )
