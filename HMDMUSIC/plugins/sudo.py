from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from config import (
    OWNER_ID,
    OWNER_NAME,
    OWNER_USERNAME,
    OWNER_BIO,
    OWNER_PHOTO
)

from HMDMUSIC.core.database import db

usersdb = db.users
groupsdb = db.groups


@Client.on_message(filters.text & filters.regex("^المطور$"))
async def owner_info(_, message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📞 التواصل",
                    url=f"https://t.me/{OWNER_USERNAME}"
                )
            ]
        ]
    )

    text = f"""
👑 معلومات المطور

• الاسم: {OWNER_NAME}
• اليوزر: @{OWNER_USERNAME}

📝 النبذة:
{OWNER_BIO}
"""

    await message.reply_photo(
        OWNER_PHOTO,
        caption=text,
        reply_markup=keyboard
    )


@Client.on_message(filters.text & filters.regex("^فحص$"))
async def ping_command(_, message):

    if message.from_user.id != OWNER_ID:
        return

    await message.reply_text(
        "✅ HMDMUSIC يعمل بنجاح"
    )


@Client.on_message(filters.text & filters.regex("^الاحصائيات$"))
async def stats_command(_, message):

    if message.from_user.id != OWNER_ID:
        return

    users = await usersdb.count_documents({})
    groups = await groupsdb.count_documents({})

    await message.reply_text(
        f"""
📊 احصائيات HMDMUSIC

👤 المستخدمين: {users}
👥 المجموعات: {groups}
"""
    )


@Client.on_message(filters.text & filters.regex("^السورس$"))
async def source_command(_, message):

    await message.reply_text(
        f"""
🎵 HMDMUSIC

🚀 إصدار 1.0

👑 المطور: {OWNER_NAME}
"""
    )
