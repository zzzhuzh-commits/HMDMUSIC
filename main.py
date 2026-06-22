from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "HMDMUSIC",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message()
async def test(_, message):
    if message.text == "هلا":
        await message.reply("هلا والله من HMDMUSIC 🎵")

app.run()
