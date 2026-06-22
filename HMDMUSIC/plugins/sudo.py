from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import OWNER_ID


@Client.on_message(filters.text & filters.regex("^المطور$"))
async def owner_panel(_, message):

    if message.from_user.id != OWNER_ID:
        return

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📊 الاحصائيات",
                    callback_data="stats"
                )
            ],
            [
                InlineKeyboardButton(
                    "📢 اذاعة",
                    callback_data="broadcast"
                )
            ],
            [
                InlineKeyboardButton(
                    "📡 فحص",
                    callback_data="ping"
                )
            ]
        ]
    )

    await message.reply_text(
        "👑 لوحة تحكم HMDMUSIC",
        reply_markup=keyboard
    )
