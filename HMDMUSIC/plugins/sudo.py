from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)

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


@Client.on_callback_query(filters.regex("^ping$"))
async def ping_callback(_, query: CallbackQuery):

    if query.from_user.id != OWNER_ID:
        return

    await query.answer(
        "✅ البوت يعمل بنجاح",
        show_alert=True
    )


@Client.on_callback_query(filters.regex("^stats$"))
async def stats_callback(_, query: CallbackQuery):

    if query.from_user.id != OWNER_ID:
        return

    await query.answer()

    await query.message.edit_text(
        """
📊 احصائيات HMDMUSIC

👤 المستخدمين: قريباً
👥 المجموعات: قريباً

🚀 HMDMUSIC
"""
    )


@Client.on_callback_query(filters.regex("^broadcast$"))
async def broadcast_callback(_, query: CallbackQuery):

    if query.from_user.id != OWNER_ID:
        return

    await query.answer(
        "📢 سيتم إضافة نظام الإذاعة قريباً",
        show_alert=True
    )
