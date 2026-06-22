from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

from HMDMUSIC.utils.pluginloader import load_plugins

app = Client(
    "HMDMUSIC",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

load_plugins()

app.run()
